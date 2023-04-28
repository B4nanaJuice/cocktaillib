### Si le serveur est déjà lancé : 
`sudo lsof -iTCP:5500 -sTCP:LISTEN`
puis `kill 12892 (dépend du PID marqué)`