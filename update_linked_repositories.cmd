git checkout immunity_product
cd content
git pull origin content
cd ..
git add .
git commit -m "Update the content submodule to the latest version of the content branch"
git push

git checkout peacemaker_product
cd content
git pull origin content
cd ..
git add .
git commit -m "Update the content submodule to the latest version of the content branch"
git push