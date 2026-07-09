import { Component } from '@angular/core';
import { Contract, JsonRpcProvider } from 'ethers';

@Component({
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  readonly rpcUrl = 'http://127.0.0.1:8545';
  readonly contractAddress = '0xbbdBD9Af93AD4DEdA28E579F644D9a27CA4A491D';
  readonly contractAbi = [
    'function set(uint256 newValue)',
    'function get() view returns (uint256)',
  ];

  storedValue = 'Not loaded yet';
  newValue = '';
  status = 'Connect Ganache on 127.0.0.1:8545, then load the deployed contract value.';
  loading = false;

  async loadValue() {
    this.loading = true;
    this.status = 'Reading value from Ganache...';
    try {
      const provider = new JsonRpcProvider(this.rpcUrl);
      const contract = new Contract(this.contractAddress, this.contractAbi, provider);
      const currentValue = await contract.get();
      this.storedValue = currentValue.toString();
      this.status = 'Loaded value from the deployed contract.';
    } catch (error) {
      this.status = 'Could not read the contract value. Check Ganache and contract address.';
      this.storedValue = 'Error';
      console.error(error);
    } finally {
      this.loading = false;
    }
  }

  async saveValue() {
    this.loading = true;
    try {
      const rawValue = this.newValue.trim();
      if (!/^\d+$/.test(rawValue)) {
        this.status = 'Enter a non-negative whole number.';
        return;
      }
      const value = BigInt(rawValue);

      const provider = new JsonRpcProvider(this.rpcUrl);
      const signer = await provider.getSigner();
      const contract = new Contract(this.contractAddress, this.contractAbi, signer);

      this.status = 'Sending transaction to the contract...';
      const transaction = await contract.set(value);
      await transaction.wait();
      this.storedValue = value.toString();
      this.status = 'Transaction confirmed. Click Load stored value to verify.';
    } catch (error) {
      this.status = 'Transaction failed. Check Ganache, contract address, and RPC access.';
      console.error(error);
    } finally {
      this.loading = false;
    }
  }
}
