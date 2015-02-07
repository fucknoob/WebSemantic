
import subprocess

proc = subprocess.Popen("php /home/mdnetsearc/public_html/get_Text.php q=http://www.globo.com", shell=True,stdout=subprocess.PIPE)

script_response = proc.stdout.read()

print script_response
