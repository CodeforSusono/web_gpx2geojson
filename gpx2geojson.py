import gpxpy
from umapgeojson import ATMFeature, AEDFeature, HospitalFeature, FreeWiFiFeature, SSWHFeature, SSFeature, BenchFeature, VMFeature, VMADFeature, ToiletFeature, InfoFeature, SideWalkFeature, BlockFenceFeature, StoneWallFeature, BridgeFeature, UnSupportedFeature, TrajectoryFeature
import geojson
import sys
import os

def getFeatures( gpx ):
    # gpxファイルに定義されたウエイポイントnameから必要な地物のみgeojsonオブジェクトに変換
    features = []
    side_walk_section = []
    block_fence_section = []
    stone_wall_section = []
    bridge_section = []
    for waypoint in gpx.waypoints:
        if waypoint.name == 'atm' or waypoint.name == 'ATM':
            atm = ATMFeature(waypoint.longitude, waypoint.latitude)
            features.append(atm.getGeoJSON())
            continue
        if waypoint.name == 'aed' or waypoint.name == 'AED':
            aed = AEDFeature(waypoint.longitude, waypoint.latitude)
            features.append(aed.getGeoJSON())
            continue
        if waypoint.name == '病院':
            hospital = HospitalFeature(waypoint.longitude, waypoint.latitude)
            features.append(hospital.getGeoJSON())
            continue
        if waypoint.name == 'freewifi' or waypoint.name == 'FreeWiFi':
            wifi = FreeWiFiFeature(waypoint.longitude, waypoint.latitude)
            features.append(wifi.getGeoJSON())
            continue
        if waypoint.name == '災害時帰宅支援ステーション':
            sswh = SSWHFeature(waypoint.longitude, waypoint.latitude)
            features.append(sswh.getGeoJSON())
            continue
        if waypoint.name == 'セーフティステーション':
            ss = SSFeature(waypoint.longitude, waypoint.latitude)
            features.append(ss.getGeoJSON())
            continue
        if waypoint.name == 'ベンチ':
            bench = BenchFeature(waypoint.longitude, waypoint.latitude)
            features.append(bench.getGeoJSON())
            continue
        if waypoint.name == '自販機':
            vm = VMFeature(waypoint.longitude, waypoint.latitude)
            features.append(vm.getGeoJSON())
            continue
        if waypoint.name == '災害対応自販機':
            vmad = VMADFeature(waypoint.longitude, waypoint.latitude)
            features.append(vmad.getGeoJSON())
            continue
        if waypoint.name == 'トイレ':
            toilet = ToiletFeature(waypoint.longitude, waypoint.latitude)
            features.append(toilet.getGeoJSON())
            continue
        if waypoint.name.startswith('高さ') or waypoint.name.startswith('段差')  or waypoint.name.startswith('幅') or waypoint.name == '未舗装' or waypoint.name == '歩道なし' :
            info = InfoFeature(waypoint.name, waypoint.longitude, waypoint.latitude)
            features.append(info.getGeoJSON())
            continue
        if waypoint.name == '歩道開始':
            if len(side_walk_section)!=0:
                print('Warning:{0}地点の情報が連続しているため処理できません.前回の情報を無視して処理します. waypoint:time:{1},longitude:{2},latitude:{3}'.format(waypoint.name,waypoint.time,waypoint.longitude,waypoint.latitude))
                side_walk_section=[]
            else:
                starting_point = { 'info':'start', 'time': waypoint.time, 'point':(waypoint.longitude, waypoint.latitude)}
                side_walk_section.append(starting_point)
            continue
        if waypoint.name == '歩道終了':
            if len(side_walk_section)!=1 or side_walk_section[0].get('info')!='start':
                print('Warning:歩道開始地点の情報がない状態で{0}地点の情報が記録されているため処理できません.今回の情報を無視して処理します. waypoint:time:{1},longitude:{2},latitude:{3}'.format(waypoint.name,waypoint.time,waypoint.longitude,waypoint.latitude))
                side_walk_section=[]
            else:
                ending_point = {'info':'end', 'time': waypoint.time, 'point':(waypoint.longitude, waypoint.latitude)}
                side_walk_section.append(ending_point)
                side_walk = SideWalkFeature( side_walk_section )
                features.append(side_walk.getGeoJSON())
            continue
        if waypoint.name == 'ブロック塀開始':
            if len(block_fence_section)!=0:
                print('Warning:{0}地点の情報が連続しているため処理できません.前回の情報を無視して処理します. waypoint:time:{1},longitude:{2},latitude:{3}'.format(waypoint.name,waypoint.time,waypoint.longitude,waypoint.latitude))
                block_fence_section=[]
            else:
                starting_point = { 'info':'start', 'time': waypoint.time, 'point':(waypoint.longitude, waypoint.latitude)}
                block_fence_section.append(starting_point)
            continue
        if waypoint.name == 'ブロック塀終了':
            if len(block_fence_section)!=1 or block_fence_section[0].get('info')!='start':
                print('Warning:ブロック塀開始地点の情報がない状態で{0}地点の情報が記録されているため処理できません.今回の情報を無視して処理します. waypoint:time:{1},longitude:{2},latitude:{3}'.format(waypoint.name,waypoint.time,waypoint.longitude,waypoint.latitude))
                block_fence_section=[]
            else:
                ending_point = {'info':'end', 'time': waypoint.time, 'point':(waypoint.longitude, waypoint.latitude)}
                block_fence_section.append(ending_point)
                block_fence = BlockFenceFeature( block_fence_section )
                features.append(block_fence.getGeoJSON())
            continue
        if waypoint.name == '石塀開始':
            if len(stone_wall_section)!=0:
                print('Warning:{0}地点の情報が連続しているため処理できません.前回の情報を無視して処理します. waypoint:time:{1},longitude:{2},latitude:{3}'.format(waypoint.name,waypoint.time,waypoint.longitude,waypoint.latitude))
                stone_wall_section=[]
            else:
                starting_point = { 'info':'start', 'time': waypoint.time, 'point':(waypoint.longitude, waypoint.latitude)}
                stone_wall_section.append(starting_point)
            continue
        if waypoint.name == '石塀終了':
            if len(stone_wall_section)!=1 or stone_wall_section[0].get('info')!='start':
                print('Warning:石塀開始地点の情報がない状態で{0}地点の情報が記録されているため処理できません.今回の情報を無視して処理します. waypoint:time:{1},longitude:{2},latitude:{3}'.format(waypoint.name,waypoint.time,waypoint.longitude,waypoint.latitude))
                stone_wall_section=[]
            else:
                ending_point = {'info':'end', 'time': waypoint.time, 'point':(waypoint.longitude, waypoint.latitude)}
                stone_wall_section.append(ending_point)
                stone_wall = StoneWallFeature( stone_wall_section )
                features.append(stone_wall.getGeoJSON())
            continue
        if waypoint.name == '橋開始':
            if len(stone_wall_section)!=0:
                print('Warning:{0}地点の情報が連続しているため処理できません.前回の情報を無視して処理します. waypoint:time:{1},longitude:{2},latitude:{3}'.format(waypoint.name,waypoint.time,waypoint.longitude,waypoint.latitude))
                bridge_section=[]
            else:
                starting_point = { 'info':'start', 'time': waypoint.time, 'point':(waypoint.longitude, waypoint.latitude)}
                bridge_section.append(starting_point)
            continue
        if waypoint.name == '橋終了':
            if len(bridge_section)!=1 or bridge_section[0].get('info')!='start':
                print('Warning:橋開始地点の情報がない状態で{0}地点の情報が記録されているため処理できません.今回の情報を無視して処理します. waypoint:time:{1},longitude:{2},latitude:{3}'.format(waypoint.name,waypoint.time,waypoint.longitude,waypoint.latitude))
                bridge_section=[]
            else:
                ending_point = {'info':'end', 'time': waypoint.time, 'point':(waypoint.longitude, waypoint.latitude)}
                bridge_section.append(ending_point)
                bridge = BridgeFeature( bridge_section )
                features.append(bridge.getGeoJSON())
            continue
        other = UnSupportedFeature(waypoint.name, waypoint.longitude, waypoint.latitude)
        features.append(other.getGeoJSON())
    # 移動経路
    for track in gpx.tracks:
        for segment in track.segments:
            trk_section=[]
            for point in segment.points:
                trk_section.append({'info':point.elevation, 'time':point.time,'point':(point.longitude, point.latitude)})
            route = TrajectoryFeature(trk_section)
            features.append(route.getGeoJSON())
    return features

def getOutputFilename(filename):
    # 出力ファイル名は拡張子.gpxを.geojsonにしたもの
    fname=filename.replace('.gpx','.geojson')
    if os.path.isfile(fname):
        # 既に同名のファイルが存在する場合は'_'を追加
        newname=fname.replace('.geojson','_.gpx')
        fname = getOutputFilename(newname)
    return fname

def convert(gpx_filename):
    # gpxファイルの読み込み
    with open(gpx_filename, 'r', encoding='utf-8') as infile:
        gpx = gpxpy.parse(infile)
    
    # 読み込んだgpxファイルをgeojsonオブジェクトに変換
    features = getFeatures(gpx)
    feature_collection = geojson.FeatureCollection(features)

    # geojsonオブジェクトをファイルに出力
    output_filename = getOutputFilename(gpx_filename)
    with open(output_filename, 'w') as outfile:
        geojson.dump(feature_collection, outfile, indent=2)


if __name__=='__main__':
    args = sys.argv
    if 2 != len(args):
        print('Usage: python %s gpx_filename' % args[0])
        print('transport gpx file to geojson for umap')
        print('output file name : (gpx_filename).geojson')
        quit()
    
    if not os.path.isfile(args[1]):
        print('Error: gpx file %s not found' % argx[1])
        quit()
    
    # 変換gpx > geojson
    convert(args[1])

    