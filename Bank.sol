// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleBank {
    address public owner;
    mapping(address => uint256) private balances;

    event Deposited(address indexed account, uint256 amount);
    event Withdrawn(address indexed account, uint256 amount);

    constructor() {
        owner = msg.sender;
    }

    // Deposit funds into sender's account
    function deposit() external payable {
        require(msg.value > 0, "Must send some ETH");
        balances[msg.sender] += msg.value;
        emit Deposited(msg.sender, msg.value);
    }

    // Withdraw up to the caller's balance
    function withdraw(uint256 amountWei) external {
        require(amountWei > 0, "Amount must be > 0");
        require(balances[msg.sender] >= amountWei, "Insufficient balance");
        balances[msg.sender] -= amountWei;
        payable(msg.sender).transfer(amountWei);
        emit Withdrawn(msg.sender, amountWei);
    }

    // View the caller's balance (in wei)
    function getMyBalance() external view returns (uint256) {
        return balances[msg.sender];
    }

}
