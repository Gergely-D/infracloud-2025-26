!/bin/bash
set -e

echo "== DEVASC YANG Lab =="

# 1. Ga naar devnet-src
cd ~/labs/devnet-src
echo "[OK] In devnet-src"

# 2. Maak pyang directory
mkdir -p pyang
cd pyang
echo "[OK] In pyang directory"

# 3. Download YANG model
YANG_URL="https://raw.githubusercontent.com/YangModels/yang/master/vendor/cisco/xe/1693/ietf-interfaces.yang"
echo "[INFO] Downloaden van ietf-interfaces.yang"
wget -q $YANG_URL

# Controle
ls -l ietf-interfaces.yang

# 4. Installeer pyang indien nodig
if ! ~/.local/bin/pyang -v >/dev/null 2>&1; then
    echo "[INFO] pyang niet gevonden, installeren..."
    pip3 install --user pyang
fi

echo "[OK] pyang versie:"
~/.local/bin/pyang -v

# 5. Transformeer YANG model
echo
echo "== PYANG TREE OUTPUT =="
echo

~/.local/bin/pyang -f tree ietf-interfaces.yang || true

# script runnen met bash automate_yang_lab.sh 