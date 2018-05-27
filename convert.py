#!/usr/bin/python

import os
import shutil

# " --rotateX90 --etc2 --mipmaps"
defaultParams = " --rotateX90 --mipmaps"

def convert(modelName, outName):
	os.system("..\\..\\..\\Tools\\MeshConverter\\MeshConverter_Release.exe Models/" + modelName + " ExternalAssets/" + outName + " " + defaultParams )

convert( "../../polly/polly/project_polly.gltf ", "Polly" );
convert( "damagedHelmet/damagedHelmet.gltf", "DamagedHelmet" );
convert( "busterDrone/busterDrone.gltf", "BusterDrone" );
convert( "kv-2_heavy_tank_1940/scene.gltf", "Tank" );
convert( "9_mm/scene.gltf", "Pistol" );
convert( "MetalRoughSpheres/MetalRoughSpheres.gltf", "MetalRoughSpheres" );
convert( "1972_datsun_240k_gt/scene.gltf", "Datsun_240k_gt" );
convert( "zis-101a_sport_1938/scene.gltf", "ZIS" );

shutil.move( "ExternalAssets", "../../../CommonMedia/ExternalAssets" );
shutil.copytree( "EnvMaps", "../../../CommonMedia/ExternalAssets/EnvMaps" );
