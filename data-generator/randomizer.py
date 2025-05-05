import generator
import percentageDatas

hitterRandomizer = generator.generatorRange(percentageDatas.hitting)

serveSpinRandomizer = generator.generatorRange(percentageDatas.serveSpin) 
rallySpinRandomizer = generator.generatorRange(percentageDatas.rallySpin)
 
serveZoneRandomizer = generator.generatorRange(percentageDatas.serveZone)  
rallyZoneRandomizer = generator.generatorRange(percentageDatas.rallyZone)