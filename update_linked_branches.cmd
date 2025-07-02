for /f %%b in ("immunity_product" "peacemaker_product") do (

    git checkout %%b
    cd content
    git pull origin content
    cd ..
    git add .
    git commit -m "Update the content submodule to the latest version of the content branch"
    git push

)