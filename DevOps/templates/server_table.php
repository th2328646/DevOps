<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <?php
       move_uploaded_file($_FILES['upload_file']['tmp_name'],'deploy/upload/' . $_FILES['upload_file']['name']); //存储上传的文件
       echo 'This data is from server!'; //返回数据，这行字将输出到iframe的body中
    ?>
</body>
</html>