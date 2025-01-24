import torch
import torchvision.transforms as transforms
from facenet_pytorch import InceptionResnetV1, MTCNN
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

# Inicializa MTCNN e modelo
mtcnn = MTCNN(image_size=160, margin=0)
model = InceptionResnetV1(pretrained='vggface2').eval()


def extract_features(img_path):
    try:
        img = Image.open(img_path)
        img_cropped = mtcnn(img)

        if img_cropped is not None:
            img_embedding = model(img_cropped.unsqueeze(0))
            return img_embedding.detach().numpy()
        else:
            return None
    except Exception as e:
        print(f"Erro ao processar {img_path}: {e}")
        return None


def get_all_image_paths(root_dir):
    image_paths = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                image_paths.append(os.path.join(root, file))
    return image_paths


# Caminho das imagens
celebrity_images_path = 'post-processed'
image_paths = get_all_image_paths(celebrity_images_path)

# Dicionário de embeddings
celebrity_embeddings = {}

# Extração de embeddings
for img_path in image_paths:
    embedding = extract_features(img_path)
    if embedding is not None:
        celebrity_embeddings[os.path.basename(img_path)] = embedding

# Imagem de teste e máscara
new_person_image_path = '/content/drive/MyDrive/Teste Daedalus/reconhecimento_facial/marcelinho_no_db.jpg'
masked_image_path = '/content/drive/MyDrive/Teste Daedalus/reconhecimento_facial/marcelinho_na_inferencia.jpg'

new_person_embedding = extract_features(new_person_image_path)
masked_embedding = extract_features(masked_image_path)

if new_person_embedding is not None:
    celebrity_embeddings['new_person'] = new_person_embedding

# Função de similaridade coseno


def cosine_similarity(embedding1, embedding2):
    embedding1 = embedding1.flatten()
    embedding2 = embedding2.flatten()
    return np.dot(embedding1, embedding2) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))


# Comparação e identificação
best_match = None
best_score = -1

if masked_embedding is not None:
    for name, embedding in celebrity_embeddings.items():
        score = cosine_similarity(masked_embedding, embedding)
        if score > best_score:
            best_match = name
            best_score = score

# Visualização dos resultados
masked_img = Image.open(masked_image_path)
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(masked_img)
plt.title(f"Imagem do Marcelinho com máscara identificada\nIdentificado como: {
          best_match}\nScore: {best_score:.2f}")

if best_match:
    new_person_img = Image.open(new_person_image_path)
    plt.subplot(1, 2, 2)
    plt.imshow(new_person_img)
    plt.title(f"Imagem do Marcelinho no banco de dados\nNome: {best_match}")

plt.show()
