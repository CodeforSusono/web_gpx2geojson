import json
import geojson

class uMapProperties:
    """
    uMapに登録した地物をGeoJSON形式にした際propertiesに登録される情報を保持するクラス
    """
    def __init__(self, name = None, desc = None, time = None, color = 'Yellow', showLabel = None, iconUrl = None, iconClass = None, weight = None):
        """
        Parameters
        ----------
        name : 地物の名称、ラベルとして表示される
        desc : 地物の概要、地物をクリックした際にラベルとともに表示される
        time : 地物の記録日時、timeとして表示される
        color : シェイプ表示プロパティの色
        showLabel : ???（いつもnullが指定されている）
        iconUrl : 表示するアイコンシンボルファイルのURL
        weight : LineString等の線の太さ
        """
        self.name = name
        self.desc = desc
        self.time = time
        self.color = color
        self.showLabel = showLabel
        self.iconUrl = iconUrl
        self.iconClass = iconClass
        self.weight = weight

    def getDict(self):
        """
        地物のpropeties情報をDict形式で返す
        Returns
        -------
        properties : dict
            地物のproperties情報
        """
        _umap_options=dict()
        _umap_options['color']=self.color
        _umap_options['showLabel']=self.showLabel
        if self.iconUrl is not None:
            _umap_options['iconUrl']=self.iconUrl
        if self.iconClass is not None:
            _umap_options['iconClass']=self.iconClass
        if self.weight is not None:
            _umap_options['weight']=self.weight
        properties=dict()
        properties['_umap_options'] = _umap_options
        properties['name'] = self.name
        if self.desc is not None:
            properties['description'] = self.desc
        if self.time is not None:
            properties['time'] = self.time
        return properties
    
    def getJSON(self):
        """
        地物のpropeties情報をJSON形式で返す
        Returns
        -------
        text : json
            地物のproperties情報
        """
        text = json.dumps(self.getDict())
        return text

class uMapFeature:
    """
    uMap用Featureの情報を保持するクラス
    """
    def __init__(self, longitude, latitude, umap_properties):
        """
        Parameters
        ----------
        longitude : 地物の名称、ラベルとして表示される
        latitude : 地物の概要、地物をクリックした際にラベルとともに表示される
        """
        self.longitude = longitude
        self.latitude = latitude
        self.uMapProperties = umap_properties
            
    def getGeoJSON(self):
        """
        uMap用Featureの情報を保持するGeoJSONオブジェクトを返す
        Returns
        -------
        feature : GeoJSON
            uMap用Featureの情報
        """
        point = geojson.Point((self.longitude, self.latitude))
        umap_prop = self.uMapProperties.getDict()
        feature = geojson.Feature(geometry=point,properties=umap_prop)
        return feature

class ATMFeature(uMapFeature):
    """
    ATMの情報を保持するクラス
    """
    name='ATM'
    desc='店名:\n利用時間:'
    color='Green'
    iconUrl='/uploads/pictogram/bank-24_1.png'

    def __init__(self, longitude, latitude):
        """
        Parameters
        ----------
        longitude : 地物の経度
        latitude : 地物の緯度
        """
        umap_prop = uMapProperties(name=ATMFeature.name, desc=ATMFeature.desc, color=ATMFeature.color, iconUrl=ATMFeature.iconUrl)
        super().__init__(longitude, latitude, umap_prop)

class AEDFeature(uMapFeature):
    """
    AEDの情報を保持するクラス
    """
    name='AED'
    desc='店名:\n利用時間:'
    color='Red'
    iconUrl='/uploads/pictogram/hospital-24.png'

    def __init__(self, longitude, latitude):
        """
        Parameters
        ----------
        longitude : 地物の経度
        latitude : 地物の緯度
        """
        umap_prop = uMapProperties(name=AEDFeature.name, desc=AEDFeature.desc, color=AEDFeature.color, iconUrl=AEDFeature.iconUrl)
        super().__init__(longitude, latitude, umap_prop)

class HospitalFeature(uMapFeature):
    """
    病院の情報を保持するクラス
    """
    name='病院'
    desc='病院名:\n利用時間:'
    color='Red'
    iconUrl='/uploads/pictogram/hospital-24-white.png'

    def __init__(self, longitude, latitude):
        """
        Parameters
        ----------
        longitude : 地物の経度
        latitude : 地物の緯度
        """
        umap_prop = uMapProperties(name=HospitalFeature.name, desc=HospitalFeature.desc, color=HospitalFeature.color, iconUrl=HospitalFeature.iconUrl)
        super().__init__(longitude, latitude, umap_prop)

class FreeWiFiFeature(uMapFeature):
    """
    FreeWiFiの情報を保持するクラス
    """
    name='FreeWiFi'
    desc='店名:\n利用時間:'
    color='DarkBlue'
    iconUrl='/uploads/pictogram/golf-24_1.png'

    def __init__(self, longitude, latitude):
        """
        Parameters
        ----------
        longitude : 地物の経度
        latitude : 地物の緯度
        """
        umap_prop = uMapProperties(name=FreeWiFiFeature.name, desc=FreeWiFiFeature.desc, color=FreeWiFiFeature.color, iconUrl=FreeWiFiFeature.iconUrl)
        super().__init__(longitude, latitude, umap_prop)

class SSWHFeature(uMapFeature):
    """
    Support Station for Walking to Home(SSWH)の情報を保持するクラス
    """
    name='災害時帰宅支援ステーション'
    desc='店名:\n利用時間:'
    color='Crimson'
    iconUrl='/uploads/pictogram/school-24-white.png'

    def __init__(self, longitude, latitude):
        """
        Parameters
        ----------
        longitude : 地物の経度
        latitude : 地物の緯度
        """
        umap_prop = uMapProperties(name=SSWHFeature.name, desc=SSWHFeature.desc, color=SSWHFeature.color, iconUrl=SSWHFeature.iconUrl)
        super().__init__(longitude, latitude, umap_prop)

class SSFeature(uMapFeature):
    """
    Safety Station(SS) の情報を保持するクラス
    """
    name='セーフティステーション'
    desc='店名:\n利用時間:'
    color='Crimson'
    iconUrl='/uploads/pictogram/school-24.png'

    def __init__(self, longitude, latitude):
        """
        Parameters
        ----------
        longitude : 地物の経度
        latitude : 地物の緯度
        """
        umap_prop = uMapProperties(name=SSFeature.name, desc=SSFeature.desc, color=SSFeature.color,  iconUrl=SSFeature.iconUrl)
        super().__init__(longitude, latitude, umap_prop)

class BenchFeature(uMapFeature):
    """
    ベンチの情報を保持するクラス
    """
    name='ベンチ'
    desc='補足:'
    color='LimeGreen'
    iconUrl='/uploads/pictogram/star-24-white.png'

    def __init__(self, longitude, latitude):
        """
        Parameters
        ----------
        longitude : 地物の経度
        latitude : 地物の緯度
        """
        umap_prop = uMapProperties(name=BenchFeature.name, desc=BenchFeature.desc, color=BenchFeature.color, iconUrl=BenchFeature.iconUrl)
        super().__init__(longitude, latitude, umap_prop)

class VMFeature(uMapFeature):
    """
    Vending Machine(自動販売機）の情報を保持するクラス
    """
    name='自動販売機'
    desc='種別:\n台数;'
    color='DodgerBlue'
    iconUrl='/uploads/pictogram/cafe-24_1.png'

    def __init__(self, longitude, latitude):
        """
        Parameters
        ----------
        longitude : 地物の経度
        latitude : 地物の緯度
        """
        umap_prop = uMapProperties(name=VMFeature.name, desc=VMFeature.desc, color=VMFeature.color, iconUrl=VMFeature.iconUrl)
        super().__init__(longitude, latitude, umap_prop)

class VMADFeature(uMapFeature):
    """
    Vending Machine Available in case of Disaster(災害時利用可能型自動販売機）の情報を保持するクラス
    """
    name='災害対応自動販売機'
    desc='種別:\n台数;'
    color='DodgerBlue'
    iconUrl='/uploads/pictogram/cafe-24.png'

    def __init__(self, longitude, latitude):
        """
        Parameters
        ----------
        longitude : 地物の経度
        latitude : 地物の緯度
        """
        umap_prop = uMapProperties(name=VMADFeature.name, desc=VMADFeature.desc, color=VMADFeature.color, iconUrl=VMADFeature.iconUrl)
        super().__init__(longitude, latitude, umap_prop)

class ToiletFeature(uMapFeature):
    """
    トイレの情報を保持するクラス
    """
    name='トイレ'
    desc='種別:\n補足:'
    color='Yellow'
    iconUrl='/uploads/pictogram/toilets-24.png'

    def __init__(self, longitude, latitude):
        """
        Parameters
        ----------
        longitude : 地物の経度
        latitude : 地物の緯度
        """
        umap_prop = uMapProperties(name=ToiletFeature.name, desc=ToiletFeature.desc, color=ToiletFeature.color, iconUrl=ToiletFeature.iconUrl)
        super().__init__(longitude, latitude, umap_prop)

class InfoFeature(uMapFeature):
    """
    補足情報を保持するクラス
    """
    color='Yellow'
    iconUrl='/uploads/pictogram/religious-jewish-24.png'
    iconClass='Drop'

    def __init__(self, name, longitude, latitude):
        """
        Parameters
        ----------
        name : 補足情報
        longitude : 地物の経度
        latitude : 地物の緯度
        """
        umap_prop = uMapProperties(name=name, color=InfoFeature.color, iconUrl=InfoFeature.iconUrl, iconClass=InfoFeature.iconClass)
        super().__init__(longitude, latitude, umap_prop)

class UnSupportedFeature(uMapFeature):
    """
    未対応アイテムの情報を保持するクラス
    """
    color='Black'
    iconClass='Ball'
    desc='未移行アイテム'

    def __init__(self, name, longitude, latitude, time=None):
        """
        Parameters
        ----------
        name : 補足情報
        longitude : 地物の経度
        latitude : 地物の緯度
        time : 記録日時
        """
        desc="{0}\nlongitude:{1}\nlatitude:{2}\ntime:{3}".format(UnSupportedFeature.desc, longitude, latitude, time)
        umap_prop = uMapProperties(name=name, desc=desc, time =time, color=UnSupportedFeature.color, iconClass=UnSupportedFeature.iconClass)
        super().__init__(longitude, latitude, umap_prop)

class uMapLineString:
    """
    uMap用LineStringの情報を保持するクラス
    """
    def __init__(self, section, umap_properties):
        """
        Parameters
        ----------
        section : array of dictionary
            地点情報{'info':info, 'time':time, 'point':(longitude, latitude)}の配列
        uMapProperties : dict
            LineStringのProperties情報
        """
        self.section = section
        self.uMapProperties = umap_properties
            
    def getGeoJSON(self):
        """
        uMap用Featureの情報を保持するGeoJSONオブジェクトを返す
        Returns
        -------
        feature : GeoJSON
            uMap用Featureの情報
        """
        points = []
        for a_section in self.section:
            points.append(a_section.get('point'))
        line= geojson.LineString( points )
        umap_prop = self.uMapProperties.getDict()
        feature = geojson.Feature(geometry=line, properties=umap_prop)
        return feature

class SideWalkFeature(uMapLineString):
    """
    歩道の情報を保持するクラス
    """
    name='歩道'
    color='Sienna'
    weight='5'

    def __init__(self, section):
        """
        Parameters
        ----------
        section : 開始地点、終了地点の時間、緯度、経度
        """
        umap_prop = uMapProperties(name=SideWalkFeature.name,color=SideWalkFeature.color,weight=SideWalkFeature.weight)
        super().__init__(section, umap_prop)

class BlockFenceFeature(uMapLineString):
    """
    ブロック塀の情報を保持するクラス
    """
    name='ブロック塀'
    color='Crimson'
    weight='5'

    def __init__(self, section):
        """
        Parameters
        ----------
        section : 開始地点、終了地点の時間、緯度、経度
        """
        umap_prop = uMapProperties(name=BlockFenceFeature.name,color=BlockFenceFeature.color,weight=BlockFenceFeature.weight)
        super().__init__(section, umap_prop)

class StoneWallFeature(uMapLineString):
    """
    石塀の情報を保持するクラス
    """
    name='石塀'
    color='OrangeRed'
    weight='5'

    def __init__(self, section):
        """
        Parameters
        ----------
        section : 開始地点、終了地点の時間、緯度、経度
        """
        umap_prop = uMapProperties(name=StoneWallFeature.name,color=StoneWallFeature.color,weight=StoneWallFeature.weight)
        super().__init__(section, umap_prop)

class BridgeFeature(uMapLineString):
    """
    橋の情報を保持するクラス
    """
    name='橋'
    color='Orange'
    weight='5'

    def __init__(self, section):
        """
        Parameters
        ----------
        section : 開始地点、終了地点の時間、緯度、経度
        """
        umap_prop = uMapProperties(name=BridgeFeature.name,color=BridgeFeature.color,weight=BridgeFeature.weight)
        super().__init__(section, umap_prop)

class TrajectoryFeature(uMapLineString):
    """
    移動軌跡の情報を保持するクラス
    """
    name='移動軌跡'
    weight='5'
    color='Black'
    
    def __init__(self, section):
        """
        Parameters
        ----------
        section : 開始地点、終了地点の時間、緯度、経度情報を持つ辞書の配列
        """
        desc="開始時刻：{0}\n終了時刻：{1}".format(section[0].get('time'),section[-1].get('time'))
        umap_prop = uMapProperties(name=TrajectoryFeature.name, desc=desc, color=TrajectoryFeature.color, weight=TrajectoryFeature.weight)
        super().__init__(section, umap_prop)