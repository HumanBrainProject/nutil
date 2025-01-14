**Technical information**
-------------------------

Nutil is written as a stand-alone Windows 64-bit application written in Qt C++, which enables the full usage of both memory and processor cores. Nutil can be downloaded and compiled from the github page. When performing batch processes, Nutil will utilise all cores available on the system.  

The external libraries that are used in Nutil are: 
 
* Libtiff for fast and efficient TIFF file handling (http://www.libtiff.org/) 
* LibXLNT for excel file IO (https://github.com/tfussell/xlnt/) 

**TiffCreator**

TiffCreator produces tiled TIFF files from JPEG, PNG and standard TIFF images, and employs the support of multiple CPUs for efficient, parallelised operations. 

**Transform** 

Transform enables rotations, scaling and thumbnail compilation of large tiff files (currently up to 4GB).  

**Quantifier**

Quantifier identifies individual binary objects in a PNG file, while matching these to output from QuickNII. The method first finds and sorts areas by using a standard pixel filler routine. Afterwards, a random area pixel is chosen as the look-up in the binary QuickNII label slice for this particular image. When all areas have been assigned a label ID, multiple selections of predefined area IDs are assembled (ID list from the excel input file), and finally output reports are assembled and written to disk (in xlsl format). In addition, original ilastik .png files with colour/ID coding added to underlying atlas slice data are assembled and saved to the output folder. 

