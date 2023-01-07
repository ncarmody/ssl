def WriteInfoFile(writeInfo, path,hostname, **kwargs):
  # write the gathered text information into .txt file in ./data directory
  with open(f"{path}/{str(hostname).replace('.', '_')}_info.txt", "w") as f:
    f.write(writeInfo)