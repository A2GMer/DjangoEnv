# 🚀 Django Docker Development Environment

Welcome to your Django development environment powered by Docker! This setup allows for easy development and deployment, ensuring consistency across different environments.

## 🌟 Features

- **Dockerized Setup**: Easily spin up your Django environment using Docker.
- **Isolated Environment**: No more "it works on my machine" issues.
- **Quick Start**: Get up and running in just a few commands.
- **Live Reload**: Automatic code reloads during development.

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## 🚀 Getting Started

Follow these steps to set up your development environment:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/A2GMer/DjangoEnv.git
   cd DjangoEnv
   ```

2. **Create a .env file**
   ```bash
   vi .env
   ```
   Add following sentence to set environment variable.

   `SRC_PATH = ./src`

3. **Build and run the Docker containers:**

   ```bash
   docker-compose up --build
   ```

4. **Get into a docker container:**

   ```bash
   docker container exec -it django bash
   ```

5. **Create a migration file**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server:**

   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

   Your Django app will be accessible at [http://localhost:8000](http://localhost:8000).

## 📂 Project Structure

Here's a quick overview of the project structure:

```
├── .devcontainer/     # Development container configuration (optional)
├── .github/           # GitHub configuration (issue templates, workflows, etc.)
├── django_project/    # Your Django project directory
├── manage.py          # Django's command-line utility
├── Dockerfile         # Docker configuration
├── docker-compose.yml # Docker Compose configuration
└── README.md          # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please fork this repository and submit a pull request.

## 💬 Contact

For any questions, feel free to reach out:

- **Email**: [a2gme1r@gmail.com](mailto:a2gme1r@gmail.com)
- **GitHub**: [A2GMer](https://github.com/A2GMer/)
