# Mp3Con

Basic mp3 file concatenator.

## Requirements

-   FFMPEG installed as an environment variable

## Folder Structure:

```
app
└── combine
```

## Usage:

-   Place mp3 files in `combine` folder to generate a concatenated mp3 file `output.mp3` inside app directory

## How it works

-   Reads files in `combine` folder
-   Creates a disposible file called `filenames.txt` to store names of all files in `combine` folder
-   Generates combined file `output.mp3` based on names in `filenames.txt` using FFMPEG
