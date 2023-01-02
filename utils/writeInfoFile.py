def WriteInfoFile(writeInfo, path,hostname, **kwargs):
  with open(f"{path}/{str(hostname).replace('.', '_')}_info.txt", "w") as f:
    f.write(writeInfo)