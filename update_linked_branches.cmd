for /f %%b in ("immunity_product" "peacemaker_product") do (

    echo Synchronizing branch %%b
    git checkout %%b
    cd content
    git pull origin content
    cd ..
    git add .
    git commit -m "Update the content submodule to the latest version of the content branch"
    git push

)

git checkout content