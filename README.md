<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Cure549/mo-menus">
    <img src="_images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Mo-Menus!</h3>

  <p align="center">
    An awesome terminal menu creator!
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Mo-Menus! is a python-based library that allows terminal menus to be created extremely easily and with a ton of customization.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

Mo-Menus! and Boxxy were created using Python 3.10.2

* [Python 3.10.2](https://www.python.org/downloads/release/python-3102/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Getting started with Mo-Menus is extremely easy. Just follow the steps below to get started.

### Prerequisites

Colorama is currently the only prerequisite needed. This allows Mo-Menus! to have support for custom colors.
* colorama
  ```py
  pip install colorama
  ```

### Installation

_Installation is very straightforward. I will soon be looking to upload this repo to pip for an easier install._

1. Clone the repo
2. Place the mo-menus and boxxy folder into your current project.
3. Import into project
   ```py
   from mo_menus.Menu import Menu
   from mo_menus.Entry import Entry
   ```
4. Create your menus as needed!

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use-cases along with examples of all possible customization can be seen in examples.py. Images of results will be added soon.

_For examples, please refer to the [examples.py](https://github.com/Cure549/mo-menus/blob/main/examples.py) file_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add experimental menu drawing
- [ ] Refactor portions of menu.py
- [ ] Add Additional Templates w/ Examples
- [ ] Refactor project to use Colorama instead of Prettify
- [ ] Finish PEP-8 Compliance
    - [ ] Mo-Menus!
    - [ ] Boxxy

See the [open issues](https://github.com/Cure549/mo-menus/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Kameryn Knight - korust549@gmail.com

Project Link: [https://github.com/Cure549/mo-menus](https://github.com/Cure549/mo-menus)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/cure549/mo-menus.svg?style=for-the-badge
[contributors-url]: https://github.com/Cure549/mo-menus/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/cure549/mo-menus.svg?style=for-the-badge
[forks-url]: https://github.com/Cure549/mo-menus/network/members
[stars-shield]: https://img.shields.io/github/stars/cure549/mo-menus.svg?style=for-the-badge
[stars-url]: https://github.com/Cure549/mo-menus/stargazers
[issues-shield]: https://img.shields.io/github/issues/cure549/mo-menus.svg?style=for-the-badge
[issues-url]: https://github.com/Cure549/mo-menus/issues
[license-shield]: https://img.shields.io/github/license/cure549/mo-menus.svg?style=for-the-badge
[license-url]: https://github.com/Cure549/mo-menus/blob/main/LICENSE.txt
[product-screenshot]: _images/screenshot.png