<?php
  ini_set('allow_url_fopen','On');

  require_once('class.html2text.inc');
  
  function Abre_Conexao() 
  {	
      @mysql_connect("dbmy0023.whservidor.com", "mindnet", "acc159753");
      @mysql_select_db("mindnet");		
  }  
  
  function fecha_busca3($usr,$url)
  {
   $url = addslashes($url );
   @mysql_query(" delete from WEB_CACHE_LINKS  where USR = '$usr'  and url= '$url' " );
  }
    
  function post_pagina2($url,$pg,$termo,$usr,$purpose )
  {

     $url = addslashes($url );
     $pg = addslashes($pg );
     $termo = addslashes($termo );
     $purpose = addslashes($purpose );

     @mysql_query("insert into WEB_CACHE (URL,PG,TERMO,USR,PURPOSE,SEMA_RESUME) values('$url','$pg','$termo','$usr','$purpose','')");
     fecha_busca3($usr,$url) ;  
  }
  
  function post_links2($url,$termo,$usr,$purpose)
  {
     $url = addslashes($url );
     $termo = addslashes($termo );
     $purpose = addslashes($purpose );
     //$purpose = mysql_real_escape_string($purpose );
     
     @mysql_query("insert into WEB_CACHE_LINKS (URL,TERMO,USR,PURPOSE,PROCESSED) values('$url','$termo','$usr','$purpose','N')");
  }
  
  $ulr='';
  if(!empty($_POST['q'] ) )
  {
    $url=$_POST['q'];
  }  
  else
  {
    $url=$_GET['q'];
  }
  
  
  $termo='';
  $usr='';
  $purpose='';
  
  
  if(!empty($_POST['termo'] ) )
  {
    $termo=$_POST['termo'];
  }  
  else
  {
    $termo=$_GET['termo'];
  }

  if(!empty($_POST['usr'] ) )
  {
    $usr=$_POST['usr'];
  }  
  else
  {
    $usr=$_GET['usr'];
  }

  if(!empty($_POST['purpose'] ) )
  {
    $purpose=$_POST['purpose'];
  }  
  else
  {
    $purpose=$_GET['purpose'];
  }
  
  Abre_Conexao();
  
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
        $h2t->set_base_url($url);
        $text1 = $h2t->get_text(); 
        $text2 = $h2t->get_links(); 
        $links = explode("\n", $text2);  
        //===========================
        post_pagina2($url,$text1,$termo,$usr,$purpose );
        //===========================
        for ( $counterk = 0; $counterk < sizeof($links) ; $counterk++ ) 
        {
          post_links2($links[$counterk],$termo,$usr,$purpose);
        }
       }
  }
  catch(Exception $e)
  {
  }
  @mysql_close();
  
?>