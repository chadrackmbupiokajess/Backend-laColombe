# Script pour copier les images depuis le frontend vers le backend
$source = "H:\Projet\AReussi\lacolombe\public\Images"
$dest = "H:\Projet\AReussi\backend_la_colombe\media"

# Services
Copy-Item "$source\f.jpeg" "$dest\services\medicine_interne.jpg"
Copy-Item "$source\2.jpeg" "$dest\services\gynecologie.jpg"
Copy-Item "$source\3.jpeg" "$dest\services\chirurgie.jpg"
Copy-Item "$source\4.jpeg" "$dest\services\pediatrie.jpg"
Copy-Item "$source\5.jpeg" "$dest\services\cardiologie.jpg"
Copy-Item "$source\6.jpeg" "$dest\services\gastroenterologie.jpg"
Copy-Item "$source\7.jpeg" "$dest\services\nephrologie.jpg"
Copy-Item "$source\f" "$dest\services\drepanocytose.jpg"
Copy-Item "$source\2.jpeg" "$dest\services\cpn.jpg"
Copy-Item "$source\3.jpeg" "$dest\services\cps.jpg"
Copy-Item "$source\4.jpeg" "$dest\services\imagerie.jpg"
Copy-Item "$source\5.jpeg" "$dest\services\laboratoire.jpg"
Copy-Item "$source\6.jpeg" "$dest\services\pharmacie.jpg"

# Équipe
Copy-Item "$source\ORT_1382.jpg.jpeg" "$dest\equipe\aminata.jpg"
Copy-Item "$source\ORT_1396.jpg.jpeg" "$dest\equipe\jean.jpg"
Copy-Item "$source\ORT_1409.jpg.jpeg" "$dest\equipe\sarah.jpg"
Copy-Item "$source\ORT_1412.jpg.jpeg" "$dest\equipe\nadine.jpg"
Copy-Item "$source\ORT_1453.jpg.jpeg" "$dest\equipe\patrick.jpg"
Copy-Item "$source\ORT_1455.jpg.jpeg" "$dest\equipe\mireille.jpg"

# Équipements
Copy-Item "$source\a.jpeg" "$dest\equipements\bloc_operatoire.jpg"
Copy-Item "$source\b.jpeg" "$dest\equipements\salle_accouchement.jpg"
Copy-Item "$source\c.jpeg" "$dest\equipements\laboratoire.jpg"
Copy-Item "$source\d.jpeg" "$dest\equipements\imagerie.jpg"
Copy-Item "$source\e.jpeg" "$dest\equipements\chambres.jpg"
Copy-Item "$source\f.jpeg" "$dest\equipements\pharmacie.jpg"

# Espaces
Copy-Item "$source\g.jpeg" "$dest\spaces\chambres.jpg"
Copy-Item "$source\3.jpeg" "$dest\spaces\3.jpegCopy-Item "$source\x.jpeg" "$dest\spaces\reception.jpg"

Write-Host "Images copiées avec succès!"
