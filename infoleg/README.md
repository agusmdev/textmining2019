## Text mining 2019 - Clustering InfoLeg

## Introduccion
Se busco hacer un analisis del corpus de InfoLeg etiquetado, buscando grupos de entidades nombradas de dominio legal con semánticas equiparables.
La idea de la implementacion es un poco rara, debido a que decidi unicamente tomar las entidades nombradas, y para sacar el contexto de cada una 

## Desarrollo del pipeline

### Preprocesamiento
Como preprocesamiento se busco separar de todo el texto legal, unicamente las entidades nombradas, utilizando expresiones regulares.

### Armado de diccionario de features
En este punto, utilizamos una idea de implementaacion 'rara' ya que para armar los features de cada entidad nombrada, se utilizó, el *POS tag* de esa entidad, junto con la entidad siguiente y anterior, segun como aparecen en el texto, con sus correspondientes *POS tags* .
Al final de todo, se 'combinaron' los features de las entidades nombradas repetidas.
    
### Vectorizacion
Para realizar la vectorizacion, se utilizo `DictVectorizer` junto con `TruncatedSVD` para la reduccion de dimensionalidad.

### Clustering
Como algoritmo de clustering se utilizo `KMeans` con una cantidad medianamente pequeña de clusters, ya que, al ser pocas entidades permite un analisis mas claro.

### Resultados - clusters
Se utilizo n = 8:

- Uno de los clusters fue:

    {'MINISTERIO DE LA PRODUCCION', 'punto 7', 'Resolución SENASA Nº 834/2002', 'Resolución N° 91/2011', 'Decreto N° 618', 'Decreto Nacional Nº 2089/93', 'Decreto Nº 1585'}
    
    Donde se esperaria que todo lo que contiene, este relacionado.
    Tenemos como primer elemento 'Ministerio de produccion', y 'Resolución SENASA Nº 834/2002' que trata del servicio nacional de sanidad y calidad agroalimentaria, por lo que estan relacionados, pero la entidad nombrada 'Resolución 91 / 2011' trata del sistema integrado previsional argentino, el cual no tiene nada que ver.

### Conclusión
En conclusión, se hizo muy complicado analizar si los resultados eran buenos o malos por la falta de dominio del problema.
Tambien se complico bastante el manejo de las entidades nombradas.
En cuanto a resultados, hubo algunos clusters con entidades relacionadas, como tambien otras que no.
Unas posibles mejoras a futuro serian, intentar entender mas el dominio del problema para poder tomar decisiones mas precisas al momento de armado de features y utilizar mas datos.