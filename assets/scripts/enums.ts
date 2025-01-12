'use strict';

enum ViewTypes {
    KnifeGrid = 1,
    SharpenerGrid = 2,
    KnifeDetail = 3,
    SharpenerDetail = 4,
    KnifeAddEdit = 5,
    SharpenerAddEdit = 6,
    BladeAddEdit = 7,
    KnifeWorkLogAddEdit = 8,
    SharpenerWorkLogAddEdit = 9,
    KnifePhotoAddEdit = 10,
    SharpenerPhotoAddEdit = 11,
    Dashboard = 12,
    Library = 13,
    LibraryAddEdit = 14
};

enum PhotoTypes {
    Knife = 1,
    Sharpener = 2,
    Library = 3
}


export { ViewTypes, PhotoTypes };