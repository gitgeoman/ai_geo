!/bin/bash
url=$(awk -F = '{print $2}' url.txt) # plik z url przygotować ręcznie
for i in $(cat url.txt);
do
wget -P ./path "${i}"
echo "${i}" | tee -a sc_res.txt
zip -FFv ./path/"${i}" --out "${i}"fixed.zip
done

cd path
unzip \*.zip
# find . -name "*.zip" -exec rm -rf {} \;