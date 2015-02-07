<?php
  ini_set('allow_url_fopen','On');

  require_once('class.html2text.inc');
  
  $ulr='';
  if(!empty($_POST['q'] ) )
  {
    $url=$_POST['q'];
  }  
  else
  {
    $url=$_GET['q'];
  }
  
  try
  {
   $htmlText = @file_get_contents($url);
   if ($htmlText == false ) 
   {
    $htmlText='';
    echo '';
   }
   else
   {
    $h2t =& new html2text($htmlText);   
    $text = $h2t->get_text(); 
    echo $text;
   }
  }
  catch(Exception $e)
  {
   echo '';
  }
  
  #$convert = explode("\n", $data); //create array separate by new line
?>