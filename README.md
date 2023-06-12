# PythonicOS

hey! before we get started, please throughly read [whatshappened.md](whatshappened.md)
it will best explain what the archived repos are for!
sorry for the inconvience with repo switching, please take care!
-charlie!
----------------
PythonicOS is an open-source operating system built on top of Arch linux and openbox. It is developed using a combination of Python and C programming languages, making it an ideal choice for developers familiar with these languages.

## Features

- **Pythonic Environment:** PythonicOS provides a familiar environment for Python developers, allowing them to leverage their existing knowledge and libraries to build applications and system components.

- **Linux Kernel:** Built on top of the reliable and robust Linux kernel, PythonicOS inherits its stability, security, and hardware compatibility features.

- **GRUB Bootloader:** PythonicOS utilizes the GRUB (GRand Unified Bootloader) to handle the boot process, providing flexibility and support for various hardware configurations.

- **Extensibility:** PythonicOS is designed with extensibility in mind. Developers can easily extend and customize the operating system by writing modules and adding new features.

## Getting Started

### Prerequisites

To build and run PythonicOS, you will need the following software installed on your system:

- Python 3.x or later

### Building PythonicOS

#### this step is not needed unless you want to build to exe with pyinstaller
  Clone the PythonicOS repository:

  git clone https://github.com/OpenStudioCorp/PythonicOS.git

  Change into the PythonicOS directory:
   
  cd PythonicOS
   
  Build the operating system using the provided build script:
   
# Running PythonicOS  

  Change into the PythonicOS directory:
  
  CD PythonicOS

  then cd into the Python directory:

  CD python

----------------------------------------------------------------------------------------------------

# Contributing

## for now controbuting is only possible on windows, mac and linux shall be added anytime if people want to contribute.
if you want to contribute, please read the following:

create a python virtual enviroment with the following naming scheme:

pythonicOS-venv-<OS>

this virtual enviroment will be used by everyone with that system type so try to keep the requirements.txt file the same between virtual enviroments.

then install the requirements.txt file with the following command if there is a requirements file:

pip install -r requirements.txt

then activate the virtual enviroment and start building!

# contributing part 2

We welcome contributions from the community to enhance PythonicOS. To contribute, please follow these steps:

Fork the PythonicOS repository.

Create a new branch for your feature or bug fix:

git checkout -b feature/your-feature-name

go into the folder that matches your Operating system, go to the scripts folder then use script provided or point your editor/IDE to the Python3.exe path

on windows the script name is "Activate.ps1"

on mac the script name is "Activate.sh"

on linux the script name is "Activate.sh"

Mac and linux scripts should have the same names, if not then feel free to change it when contributing.

Make the necessary changes and commit them:

git commit -m "Add your commit message here"

Push your changes to your forked repository:

git push origin feature/your-feature-name

Open a pull request in the original PythonicOS repository, describing your changes and their purpose.
------------------------------------------------------------------------------------------------------
License
PythonicOS is released under the OpenStudio License.

it is still a work in progress, so please be patient with us!

for now PythonicOS is released under the MIT license, but will be changed to the OpenStudio License when it is ready for release!

Contact
For any questions, suggestions, or feedback, please reach out to us at our discord,

https://discord.gg/7cFCB8qBkf