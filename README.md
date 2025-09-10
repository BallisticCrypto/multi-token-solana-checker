# Multi-Token Solana Balance Checker 🪙

This Python script fetches the balances of multiple SPL tokens for a given Solana wallet using the public RPC endpoint.

## 📋 Features

- Supports any SPL token (USDC, USDT, BONK, WETH, etc.)
- Uses Solana's public `getTokenAccountsByOwner` API
- No Solana SDK needed (uses `requests` only)

## 🚀 How to Use

1. Clone the repository or copy the code into your environment
2. Install `requests` if not already installed:

```bash
pip install requests
