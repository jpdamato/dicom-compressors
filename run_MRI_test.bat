zstd_DicomCompress_R -in  "./"  -format PNG -residual
zstd_DicomCompress_R -in  "./"  -format JPG -residual
zstd_DicomCompress_R -in  "./"  -format JP2 -residual
zstd_DicomCompress_R -in  "./"  -format MP4 -residual -visual
zstd_DicomCompress_R -in  "./"  -format ZSTD -residual
zstd_DicomCompress_R -in  "./"  -format ZIP -residual


depthCompression_r -metrics  -out "./1/fit/" -in "./1/png/" -test1 -residual
depthCompression_r -metrics  -out "./2/fit/" -in "./2/png/" -test1 -residual
depthCompression_r -metrics  -out "./3/fit/" -in "./3/png/" -test1 -residual
depthCompression_r -metrics  -out "./4/fit/" -in "./4/png/" -test1 -residual
depthCompression_r -metrics  -out "./5/fit/" -in "./5/png/" -test1 -residual
depthCompression_r -metrics  -out "./6/fit/" -in "./6/png/" -test1 -residual
depthCompression_r -metrics  -out "./7/fit/" -in "./7/png/" -test1 -residual
depthCompression_r -metrics  -out "./8/fit/" -in "./8/png/" -test1 -residual
depthCompression_r -metrics  -out "./9/fit/" -in "./9/png/" -test1 -residual
depthCompression_r -metrics  -out "./10/fit/" -in "./10/png/" -test1 -residual


