// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MyERC1155 is ERC1155, Ownable {
    constructor() ERC1155("https://ipfs.io/ipfs/Qmf3whjtx6UnNcZLCHcYVqj6DkLWLpAbQJnaT1iPpBe5vZ?filename=something.json") Ownable(msg.sender) {
        _mint(msg.sender, 1, 10, ""); // Mint 10 tokens of type 1 and assign to contract deployer
    }

    function mint(address account, uint256 id, uint256 amount, bytes memory data) public onlyOwner {
        _mint(account, id, amount, data);
    }

    function mintBatch(address to, uint256[] memory ids, uint256[] memory amounts, bytes memory data) public onlyOwner {
        _mintBatch(to, ids, amounts, data);
    }

    function setURI(string memory newuri) public onlyOwner {
        _setURI(newuri);
    }
}