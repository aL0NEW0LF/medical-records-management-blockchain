# Medical Records Management Blockchain

To start off, clone this branch of the repo into your local:
```shell
git clone https://github.com/aL0NEW0LF/medical-records-management-blockchain
```
After cloning the project, create your virutal environment:
```shell
cd medical-records-management-blockchain
```
## Setting up the environment
### Python
To create a virtual environment, run the following command in the root directory of the project:
**Windows**

```shell
py -3 -m venv .venv
```

**MacOS/Linus**

```shell
python3 -m venv .venv
```

Then, activate the env:

**Windows**

```shell
.venv\Scripts\activate
```
**MacOS/Linus**
```shell
. .venv/bin/activate
```
You can run the following command to install the dependencies:
```shell
pip3 install -r requirements.txt
```
### Hardhat
To run the GUI, you need to have a local blockchain running. We will be using Hardhat for this purpose. To install Hardhat, you need to have Node.js installed. You can download Node.js from [here](https://nodejs.org/en/download/). After installing Node.js, follow the steps below to install Hardhat:
Initialize an npm project:
```shell
npm init -y
```
Install Hardhat:
```shell
npm install --save-dev hardhat
```
Run the following command to initialize Hardhat:
```shell
npx hardhat
```
Run the hardhat node:
```shell
npx hardhat node
```
### IPFS
To run the GUI, you need to have IPFS running. You can download IPFS Desktop from [here](https://docs.ipfs.io/install/ipfs-desktop/).

The GUI uses IPFS to store the files, you need to have IPFS running in the background. And since python doesn't have a native IPFS library, and the ipfs-http-client library is not compatible with the latest version of IPFS, you need to modify the modify the `client\__init__.py` and change maximum version to the current version of IPFS running on your machine. The line should look something like this:
```python
VERSION_MAXIMUM   = "0.32.2"
```
> [!NOTE]
> This is fix is working as of the time of writing this README, until the ipfs-http-client library is updated to support the latest version of IPFS, or an official library is released.
## Running the GUI
1. Deploy the contracts to the local network in the following order as some contracts depend on others:
- RoleContract.sol
- AuditContract.sol
- PatientContract.sol
- DoctorContract.sol
2. Make sure to copy the contract addresses and ABI's to the .env file as shown in the .env.example file (The ABI's should be compacted into a single line JSON)
3. Run the GUI using the following command:
```shell
python .\GUI\App.py
```
