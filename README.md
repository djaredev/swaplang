<div align="center">
  <h1 style="">Swaplang</h1>
  <h3>Local translator similar to Google Translate, but powered by AI.</h3>
</div>

## 🧩 Technology Stack

### ⚙️ Backend

* 🐍 **Programming Language**

  * Python as the primary backend language

* 🚀 **Web Framework**

  * ⚡ **FastAPI** for building high-performance, asynchronous APIs

    * 🗄️ **SQLModel** for database modeling and ORM functionality
    * 📐 **Pydantic** for data validation, schema definition and settings management
    * 💾 **SQLite** as a relational database

* 🧠 **AI Translation Pipeline**

  * 🔥 **LLamacpp** for large language model inference
  * 🤖 **Huggingface Hub** to download models

* 🔐 **Authentication & Security**

  * 🔒 **JWT (JSON Web Tokens)** for stateless authentication for secure API access
  * 🔑 **Passlib** for password hashing with bcrypt algorithm

### 🎨 Frontend

* 🟦 **Programming Language**

  * TypeScript for type-safe frontend development

* 🧩 **Frameworks & Libraries**

  * ⚡ **Svelte** and **SvelteKit** for building a modern, reactive user interface
  * 🎨 **Vanilla CSS** for lightweight, framework-agnostic styling

### 🚀 DevOps & Infrastructure

* 📦 **Containerization**

  * 🐳 **Docker** and **Docker Compose** for development and deployment
  * 🧱 Prebuilt Docker images optimized for:

    * 🧠 CPU and 🎮 GPU (CUDA) execution
    * 🖥️ Multi-architecture support (amd64 / arm64)

* 🔁 **CI/CD**

  * 🤖 **GitHub Actions** for automated build and release pipelines
  * 📤 Continuous publishing of images to **GitHub Container Registry**

## ✨ Features

- [X] 💬 **Text translation**: Translate text into different languages.
- [X] ⏰ **Translation History**: The latest translations are saved as history.
- [x] 🖨️ **App Settings**: Various settings for the user and translation.
- [x] 🏠 **100% Self-Hosted**: Your data never leaves your server.
- [x] 🤖 **Local AI:**: Fully offline AI processing.
- [x] 🎨 **Modern UI**: A user-friendly, modern interface like Google Translator.

## 🚀 Quick Installation

### Using Docker Compose (Recommended)

Create a `docker-compose.yaml` file with the following content:

```yaml
services:
    swaplang:
        container_name: swaplang
        # image: ghcr.io/djaredev/swaplang:latest # for CPU
        image: ghcr.io/djaredev/swaplang:latest-gpu
        user: 1000:1000 # Change 1000:1000 to your user ID and group ID
        ports:
            - "3737:3737"
        volumes:
            - ./data:/data # Change ./data to the directory where you want the data to be stored persistently.
        restart: unless-stopped
```

In the directory where `docker-compose.yaml` is located, run:

```bash
docker-compose up -d
```

### Using Docker CLI

```bash
docker run -d \
  --name swaplang \
  -u 1000:1000 \
  -p 3737:3737 \
  -v ./data:/data \
  --restart unless-stopped \
  ghcr.io/djaredev/swaplang:latest-gpu
```

### Building the Docker Images locally

Clone the repository and navigate into it

```bash
git clone https://github.com/djaredev/swaplang.git
cd swaplanag/
```

### Building Docker Image with docker build

Run the following command

For GPU (CUDA):

```bash
docker build -f docker/Dockerfile --target gpu -t swaplang:gpu .
```

For CPU:

```bash
docker build -f docker/Dockerfile --target cpu -t swaplang:cpu .
```


## 📱 Usage 

Once Doc-chat has started successfully, you can access the application at:

[http://localhost:3737](http://localhost:2727)
