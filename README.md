<!-- ABOUT THE PROJECT -->
## About The Project

Hello!
This project is a simple flask application that mimics a mini at-runtime database. The database stores a Product ID and a Product in the form {id: #, Product: some_item}. Users can interact with the web framework by retrieving products, posting a new product, deleting products, etc. 

Nginx is used as a reverse proxy to forward request to our application. Docker is used to containerize our Python application.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

Python
Flask
Docker
Nginx

<p align="right">(<a href="#top">back to top</a>)</p>

### Prerequisites

Make sure you have Docker and Python installed on your computer. Postman or the Command Line Interface can be used to send requests to this application.

To start an instance of this application

### Installation

1.  Clone the repo
   ```sh
   git clone https://github.com/Kurany/Docker-Web-App.git
   ```
2. To start an instance of this application, open the project in an IDE (VS Code) or locate the project on the CLI.
3. (Optional) Create a virtual environment
   ```sh
   python3 -m venv venv
   ```
3a. (Optional) Start a virtual environment
   ```sh
   source ./venv/bin/activate
   ```
4. Build and run the docker image
   ```sh
   docker-compose up -d
   ```
5. To stop the running containers
   ```sh
   docker-compose down
   ```
6. Exit out of the virtual environment
   ```sh
   deactivate
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

1.  To return all the currently available products
   ```sh
   curl -v http://localhost/products
   ```
   [![Get Screen Shot][get-screenshot]]
2. To post a new product
   ```sh
   curl --header "Content-Type: application/json" --request POST --data '{"Product": "some product"}' -v http://localhost/product
   ```
   [![Post Screen Shot][post-screenshot]]
3. The rest can be found in application.py

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Add mySQL for data persistence
    - [ ] Done with SQL Alchemy

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - kuiny.tran@gmail.com

Project Link: [https://github.com/Kurany/Docker-Web-App](https://github.com/Kurany/Docker-Web-App)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Kurany/Docker-Web-App.svg?style=for-the-badge
[contributors-url]: https://github.com/Kurany/Docker-Web-App/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Kurany/Docker-Web-AppebApp.svg?style=for-the-badge
[forks-url]: https://github.com/Kurany/Docker-Web-App/network/members
[stars-shield]: https://img.shields.io/github/stars/Kurany/Docker-Web-App.svg?style=for-the-badge
[stars-url]: https://github.com/Kurany/Docker-Web-App/stargazers
[issues-shield]: https://img.shields.io/github/issues/Kurany/Docker-Web-App.svg?style=for-the-badge
[issues-url]: https://github.com/Kurany/Docker-Web-App/issues
[license-shield]: https://img.shields.io/github/license/Kurany/Docker-Web-App.svg?style=for-the-badge
[license-url]: https://github.com/Kurany/Docker-Web-App/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/kiettran1
[get-screenshot]: images/get.png
[post-screenshot]: images/post.png