# Local CI/CD Pipeline with GitHub Actions for Python Flask App

This project demonstrates a Continuous Integration and Continuous Deployment (CI/CD) pipeline using GitHub Actions with **local runners**. This setup allows for deployments directly to the local development environment where the code is being edited, providing a fast feedback loop during development.

## Current Stage

Currently, the project consists of a simple **Python Flask** application that interacts with a **MongoDB** database. The CI/CD pipeline itself is still under development.  This initial phase focuses on setting up the application and preparing for pipeline implementation.

## Containerization Strategy

The application, database, and web server are each deployed within separate Docker containers. The application runs in a **Flask** container, the database resides in a **MongoDB** container, and the web server utilizes an **Nginx** container.  This containerized approach provides several advantages:
- **Isolation**, ensuring that each component operates within its own environment and dependencies don't conflict;
- **Portability**, allowing the entire system to be easily moved and deployed across different environments; 
- **Scalability**, simplifying scaling individual components independently as needed; 
- **Reproducibility**, guaranteeing consistent behavior across development, testing, and production environments.

## Security

This project prioritizes security by leveraging Docker Compose's `secrets` functionality for sensitive information management. This approach offers several key advantages:

* **Secret Storage:** Database credentials (usernames and passwords) are stored outside of the application's image, codebase, and version control system, residing in files external to the container. This prevents accidental exposure in repositories like Git or build logs.

* **Access Control:**  Docker Compose manages access to the secrets, ensuring that only authorized containers can access the required credentials.  This limits the potential impact of a compromised container.

* **Version Control Best Practices:** The `.secrets` directory, containing the files with sensitive data, is included in `.gitignore`. This guarantees that these credentials are never accidentally committed to version control, protecting them from exposure in public or shared repositories.

* **Improved Portability and Maintainability:** Decoupling secrets from the application image improves portability and simplifies maintenance.  Images can be shared more safely without the risk of embedded credentials being inadvertently exposed.

While Docker Compose's `secrets` functionality doesn't provide encryption at rest like Docker Swarm secrets, it significantly improves security compared to storing credentials directly in application code or configuration files. It provides a good balance between security and ease of use for development environments.

For production environments or even stronger security during development, consider using a dedicated secrets management solution like HashiCorp Vault, AWS Secrets Manager, or Google Cloud Secret Manager.

## Application Details

* **Framework:** Python Flask
* **Database:** MongoDB
* **Webserver:** Nginx

## Next Steps - CI/CD Pipeline Implementation

The next phase of this project will involve creating the CI/CD pipeline using GitHub Actions and local runners.  The planned pipeline will include the following steps:

* **Build:** Build the Python application and its dependencies.
* **Test:** Execute unit and integration tests.
* **Deploy:** Deploy the application locally

## Goals of using Local Runners

* **Fast Feedback Loop:** Quickly test changes locally without requiring a separate deployment environment.
* **Simplified Development Setup:** Ideal for development and testing where a full remote deployment isn't necessary.
* **Cost-Effective Learning and Experimentation:** Local execution provides an ideal environment for learning and experimenting with containerization and CI/CD pipelines, without requiring investment in cloud resources.

## Getting Started

These instructions assume you have Docker and Docker Compose installed on your system.

1. **Clone the repository:**

    ```bash
    git clone https://github.com/wcruz-br/ci-cd-pipeline-github-actions-local-runner.git
    cd ci-cd-pipeline-github-actions-local-runner
    ```

2. **Docker Secrets:**
    Create a directory named `.secrets` in the root of the project. Inside this directory, create the following files, each containing the corresponding value:
    - `.secrets/db_root_user.txt`: MongoDB root username (*root*, maybe?)
    - `.secrets/db_root_password.txt`: MongoDB root password
    - `.secrets/db_app_user.txt`: MongoDB application username
    - `.secrets/db_app_password.txt`: MongoDB application password

3. **Build and run the containers:**

    This command will build the images for the application, database, and web server if they don't already exist locally, and then start the containers in detached mode (running in the background).
    ```bash
    docker-compose up -d --build
    ```
    
4. **Access the application:**

    Once the containers are running, you can access the Flask application through your web browser at http://localhost:80.

## Contributing

Contributions are welcome! Please feel free to open issues and pull requests.
