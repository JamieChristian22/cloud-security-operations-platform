"""Install fixed Linux AMD64 scan tools; verify archives against recorded SHA256."""
import hashlib,io,json,os,platform,tarfile,urllib.request,zipfile
from pathlib import Path

def main():
 if platform.system()!='Linux' or platform.machine() not in ('x86_64','amd64'):raise SystemExit('Linux AMD64 only; install native tools manually elsewhere')
 root=Path(__file__).resolve().parents[2];destination=root/'.ci-tools';destination.mkdir(exist_ok=True)
 manifest=json.loads(Path(__file__).with_name('tool-downloads.json').read_text())
 for name,item in manifest.items():
  with urllib.request.urlopen(item['url'],timeout=120) as response:payload=response.read()
  if hashlib.sha256(payload).hexdigest()!=item['sha256']:raise SystemExit(f'{name}: archive checksum mismatch')
  if item['url'].endswith('.zip'):
   with zipfile.ZipFile(io.BytesIO(payload)) as archive:data=archive.read(name)
  else:
   with tarfile.open(fileobj=io.BytesIO(payload)) as archive:data=archive.extractfile(name).read()
  target=destination/name;target.write_bytes(data);target.chmod(0o755)
 if os.environ.get('GITHUB_PATH'):
  with open(os.environ['GITHUB_PATH'],'a') as output:output.write(str(destination)+'\n')
 print(destination)
if __name__=='__main__':main()
