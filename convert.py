#!/usr/bin/python

import os
import shutil

# " --etc2 --mipmaps"
defaultParams = " --mipmaps"

def convert(modelName, outName, params = ""):
	if os.system("..\\..\\..\\Tools\\MeshConverter\\MeshConverter_Release.exe Models/" + modelName + " ExternalAssets/" + outName + " " + defaultParams + " " + params ) != 0:
		print("Failed to run MeshConverter")
		exit(255)

convert( "../../polly/polly/project_polly.gltf", "Polly" );
convert( "../../gltf-test/tutorialModels/AlphaBlendModeTest/glTF/AlphaBlendModeTest.gltf", "AlphaBlendModeTest" );
convert( "../../gltf-test/tutorialModels/AnimatedCube/glTF/AnimatedCube.gltf", "AnimatedCube" );
convert( "../../gltf-test/tutorialModels/NormalTangentTest/glTF/NormalTangentTest.gltf", "NormalTangentTest" );
convert( "../../gltf-test/tutorialModels/NormalTangentMirrorTest/glTF/NormalTangentMirrorTest.gltf", "NormalTangentMirrorTest" );
convert( "../../gltf-test/tutorialModels/OrientationTest/glTF/OrientationTest.gltf", "OrientationTest" );
convert( "../../gltf-test/tutorialModels/VertexColorTest/glTF/VertexColorTest.gltf", "VertexColorTest" );
convert( "../../gltf-test/tutorialModels/TextureSettingsTest/glTF/TextureSettingsTest.gltf", "TextureSettingsTest" );
convert( "../../glTF-Sample-Models/2.0/Sponza/glTF/Sponza.gltf", "crytek-sponza" );
convert( "damagedHelmet/damagedHelmet.gltf", "DamagedHelmet" );
convert( "busterDrone/busterDrone.gltf", "BusterDrone" );
convert( "kv-2_heavy_tank_1940/scene.gltf", "Tank" );
convert( "9_mm/scene.gltf", "Pistol" );
convert( "MetalRoughSpheres/MetalRoughSpheres.gltf", "MetalRoughSpheres" );
convert( "1972_datsun_240k_gt/scene.gltf", "Datsun_240k_gt" );
convert( "zis-101a_sport_1938/scene.gltf", "ZIS" );
convert( "Maple/Maple.obj", "Tree1_PBR", "--pbr" );

shutil.move( "ExternalAssets", "../../../CommonMedia/ExternalAssets" );
shutil.copytree( "EnvMaps", "../../../CommonMedia/ExternalAssets/EnvMaps" );
shutil.copytree( "HeightMaps", "../../../CommonMedia/ExternalAssets/HeightMaps" );
