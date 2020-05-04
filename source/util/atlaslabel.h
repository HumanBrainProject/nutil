#ifndef ATLASLABEL_H
#define ATLASLABEL_H

#include <QString>
#include <QVector3D>
#include <QStringList>
#include <QMap>
#include <QFile>
#include <QTextStream>
#include <QVector>
#include "source/util/lmessage.h"
#include <QDebug>


class AtlasLabel
{
public:
    AtlasLabel();

    QString name;
    long index;
    QVector3D color;
    QVector3D extra;
    QVector3D extra2;
    bool toggle = false;
    double maxval = 0;
    int count = 0;

    QMap<int, double> sliceArea;
    QMap<int, double> sliceAreaScaled;


    double area = 0.0;
    double areaScaled = 0.0;
    double areaSum = 0.0;


    AtlasLabel (QStringList& s)
    {
        index = s[0].toLong();
        color.setX(s[1].toFloat());
        color.setY(s[2].toFloat());
        color.setZ(s[3].toFloat());


        extra.setX(s[4].toFloat());
        extra.setY(s[5].toFloat());
        extra.setZ(s[6].toFloat());
        name = "";
        for (int i=7;i<s.count();i++)
            name = name + s[i] + " ";

        name = name.replace("\"","");
        name = name.trimmed();
        toggle = true;
        area = 0.0;
        areaScaled = 0.0;
        areaSum = 0.0;
    }
};


class AtlasLabels {
private:
    QMap<long, AtlasLabel*> indexedID;

public:
    //QMap<QVector3D, AtlasLabel*> indexedColor;
    QVector<AtlasLabel*> atlases;

    AtlasLabels() {

    }

    AtlasLabel* get(long index, bool newFormat);

    AtlasLabels(QString filename) {
        Load(filename);
    }
    void Load(QString filename);
    void LoadFake();
    void BuildDictionary();
    QVector<AtlasLabel*> getFromColor(QVector3D col);

    void Clear();

    ~AtlasLabels() {
        Clear();
    }

};

#endif // ATLASLABEL_H
