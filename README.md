# PythonicOS

hey! before we get started, please throughly read [whatshappened.md](whatshappened.md)
it will best explain what the archived repos are for!
sorry for the inconvience with repo switching, please take care!
-charlie!
----------------
PythonicOS is an open-source operating system built on top of the Linux kernel and the GRUB bootloader. It is developed using a combination of Python and C programming languages, making it an ideal choice for developers familiar with these languages.

## Features

- **Pythonic Environment:** PythonicOS provides a familiar environment for Python developers, allowing them to leverage their existing knowledge and libraries to build applications and system components.

- **Linux Kernel:** Built on top of the reliable and robust Linux kernel, PythonicOS inherits its stability, security, and hardware compatibility features.

- **GRUB Bootloader:** PythonicOS utilizes the GRUB (GRand Unified Bootloader) to handle the boot process, providing flexibility and support for various hardware configurations.

- **Extensibility:** PythonicOS is designed with extensibility in mind. Developers can easily extend and customize the operating system by writing modules and adding new features.

## Getting Started

### Prerequisites

To build and run PythonicOS, you will need the following software installed on your system:

- Linux kernel source code
- GRUB bootloader
- Python 3.x or later
- requirements from the requirements.txt file, you can install them using Pip install -R requirements.txt

### Building PythonicOS

  Clone the PythonicOS repository:

  git clone https://github.com/OpenStudioCorp/PythonicOS.git

  Change into the PythonicOS directory:
   
  cd PythonicOS
   
  Build the operating system using the provided build script:
   
  #Running PythonicOS

Install the GRUB bootloader on a bootable device (e.g., USB drive) using the following command:

grub-install /dev/sdX

Replace /dev/sdX with the appropriate device identifier for your system.

Copy the generated kernel image and configuration files to the bootable device.

Reboot your system and select the bootable device as the boot source in your BIOS or UEFI settings.
----------------------------------------------------------------------------------------------------

# Contributing

We welcome contributions from the community to enhance PythonicOS. To contribute, please follow these steps:

Fork the PythonicOS repository.

Create a new branch for your feature or bug fix:

git checkout -b feature/your-feature-name

Make the necessary changes and commit them:

git commit -m "Add your commit message here"

Push your changes to your forked repository:

git push origin feature/your-feature-name

Open a pull request in the original PythonicOS repository, describing your changes and their purpose.
------------------------------------------------------------------------------------------------------
License
PythonicOS is released under the MIT License.

Contact
For any questions, suggestions, or feedback, please reach out to us at our discord,
