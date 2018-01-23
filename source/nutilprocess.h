#ifndef NUTILPROCESS_H
#define NUTILPROCESS_H

#include <QString>
#include <QDebug>
#include <omp.h>
#include "source/util/counter.h"
#include "source/ltiff.h"
#include "source/util/util.h"
#include "source/util/counter.h"
#include "source/util/limage.h"

class NutilProcess
{
public:
    QString m_infoText;
    NutilProcess();
    int m_id;
    float getProgress();
    Counter m_counter;
    LTiff otif;

    LImage lImage;
    bool InitializeCounter(QString inFile, bool autoClip, int thumbnailSize);
    bool TransformTiff(QString inFile, QString outFile, QString compression, float angle, float scale, QColor background, bool autoClip);
    bool AutoContrast(QString inFile, QString outFile, QString compression, QColor background);
    bool GenerateThumbnail(QString inFile, QString outFile, int thumbnailSize);
    bool AutoAdjustImageLevels(QString inFile, QString outFile);

    bool PCounter(QString inFile, QColor counter);

//    m_processes[i]->PCounter(+ pi->m_inFile, m_inputDir, m_background, pi->m_outFile, m_AtlasDir, m_labelFile);

    bool LoadAndVerifyTiff(LTiff& tif, QString filename, int& writeCompression, QString compression);
};

#endif // NUTILPROCESS_H
