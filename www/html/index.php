<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Acesso por impressao digital</title>
    <meta name="generator" content="Google Web Designer 7.1.1.1210">
    <style type="text/css">
      html, body {
        width: 90%;
        height: 100%;
        margin: 0;
        style.cursor: 'none';
      }

      body {
        background: url('https://static.wixstatic.com/media/16e618_63547dd8368e440680f2911b3e911640~mv2.jpg/v1/fill/w_576,h_800/background.jpg') no-repeat;
        background-size: 345px 500px;
      }
      selector { cursor: none; };
    </style>
  </head>
  <body>
  <table>
  <tbody>
  <tr>
  <td>
  <div id="exec"><?php shell_exec("sudo /usr/bin/python /var/www/html/main.py -sqlSrc> /dev/null 2>&1 & echo $!") ?></div>
  <div id="show"><?php include 'msg.txt' ; ?></div>
  <p>&nbsp;</p>
  </td>
  </tr>
  <tr>
  <td width="345" height="300"><div id="centro"><img src="./imgs/LogoMRD3d.png" alt="*" width="326" height="264" /></div></td>
  </tr>
  <tr>
  <td style="text-align: center;"><a href="#" onclick="trocaDiv();"><img id="button" src="./imgs/addButton.png" width="50" height="50"></a></td>
  </tbody>
  </table>
  <script src="http://code.jquery.com/jquery-3.1.1.js"></script>
	<script type="text/javascript">
    var divAtual = 1;
    function trocaDiv(){
      if (divAtual == 1) {
        $.get("adduser.html", function( data ){
        $('#centro').html(data);
        $('#button').attr('src',"./imgs/menuButton.png");
        doRefresh();
        divAtual = 2;
        });
        $.ajax({type: 'post',url:'escrita.php',data: {
          'modo': 'escrita',
          'id': 'nada'
        }});
      } else {
        $('#centro').html('<img src="./imgs/LogoMRD3d.png" alt="*" width="326" height="264" />');
        $('#button').attr('src',"./imgs/addButton.png");
        $('#exec').load("execMain.php");
        doRefresh();
        divAtual = 1;
        $.ajax({type: 'post',url:'escrita.php',data: {
          'modo': 'leitura',
          'id': 'nada'
        }});
      }
    };
    function doRefresh(){
        $("#show").load("msg.txt");
    }
    $(function() {
        setInterval(doRefresh, 800);
    });
</script>
</body>
</html>
