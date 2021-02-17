function substitute_variables(){
    dist_path=$(realpath $1)
    filename=$(ls ${dist_path}/js/app*.js)

    for row in $(env | grep VUE_APP_)
    do
        variable=$(echo $row | cut -f1 -d=)
        value=$(echo $row | cut -f2 -d=)
        sed "s|<$variable>|$value|g" -i $filename
    done
}

substitute_variables $1
nginx -g "daemon off;"
