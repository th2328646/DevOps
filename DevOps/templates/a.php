<html>
<body>

    <?php
        if (!empty($_POST["operations"])){
            $operations = $_POST["operations"]
            if (!empty($_POST["package"])){
                    $show = $_POST["package"]
                } elseif (!empty($_POST["func"])){
                    $show = $_POST["func"]
                } elseif (!empty($_POST["dp_type"])){
                    $show = $_POST["dp_type"]
                } else{
                    echo "Please make your choice."
                }
        } else{
            echo "Please make your choice."
        }
        echo $show
    ?>

</body>
</html>
