run:
	uvicorn shopping_list.main:app --reload

run-https:
	uvicorn shopping_list.main:app --reload --port 8000 --ssl-keyfile key.pem --ssl-certfile cert.pem

# Generate a Private Key
key:
	openssl genpkey -algorithm RSA -out key.pem

# Generate a Certificate Signing Request (CSR)
csr:
	openssl req -new -key key.pem -out csr.pem -subj "/CN=127.0.0.1"

# Generate a Self-Signed Certificate
certificate:
	openssl x509 -req -days 365 -in csr.pem -signkey key.pem -out cert.pem


