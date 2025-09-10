import requests

# --- RPC Endpoint ---
RPC_URL = "https://api.mainnet-beta.solana.com"

# --- Wallet Address ---
WALLET = "3eURboCzqqs3UBALFKmKBB91gqTjnLTraUE5oNGtF7sH"

# --- Token Mint Addresses (add more as needed) ---
TOKENS = {
    "USDC": "Es9vMFrzaCERcAqB5kWz3P3wS6B5sZQ6R9fL9h7bSyKk",
    "USDT": "BQZT9Bz1ywTgSvoZKxRgUnTQnRtG9yxUuZ5vpNHHFPrM",
    "BONK": "DezXJw8xZ7q5vThNzfD1owEwFgfddq4Fh8Xi1A2RAGtn",
    "WETH": "7vfCXTazEByqQyCya4hEFp7B9TzTzD8ZtnoqDN3nPAsy"
}

def get_token_accounts(wallet, token_mint):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getTokenAccountsByOwner",
        "params": [
            wallet,
            {"mint": token_mint},
            {"encoding": "jsonParsed"}
        ]
    }
    response = requests.post(RPC_URL, json=payload).json()
    return response.get("result", {}).get("value", [])

def get_token_balance(wallet, token_mint):
    accounts = get_token_accounts(wallet, token_mint)
    total = 0
    for acc in accounts:
        amount = acc["account"]["data"]["parsed"]["info"]["tokenAmount"]
        ui_amount = float(amount["uiAmountString"])
        total += ui_amount
    return total

# --- Run ---
print(f"📦 Token balances for wallet {WALLET}:\n")

for name, mint in TOKENS.items():
    try:
        balance = get_token_balance(WALLET, mint)
        print(f"✅ {name}: {balance}")
    except Exception as e:
        print(f"❌ Error fetching {name}: {e}")

