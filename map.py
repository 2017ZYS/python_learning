#import pygal.maps.world
#
#worldmap_chart = pygal.maps.world.World()
#worldmap_chart.title = 'Some countries'
#worldmap_chart.add('F countries', ['fr', 'fi'])
#worldmap_chart.add('M countries', ['ma', 'mc', 'md', 'me', 'mg',
#                                   'mk', 'ml', 'mm', 'mn', 'mo',
#                                   'mr', 'mt', 'mu', 'mv', 'mw',
#                                   'mx', 'my', 'mz'])
#worldmap_chart.add('U countries', ['ua', 'ug', 'us', 'uy', 'uz'])
#worldmap_chart.render_to_file('bar_chart.svg')



import pygal.maps.world

worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = 'Minimum deaths by capital punishement (source: Amnesty International)'
worldmap_chart.add('In 2012', {
  'af': 14,
  'bd': 1,
  'by': 3,
  'cn': 1000,
  'gm': 9,
  'in': 1,
  'ir': 314,
  'iq': 129,
  'jp': 7,
  'kp': 6,
  'pk': 1,
  'ps': 6,
  'sa': 79,
  'so': 6,
  'sd': 5,
  'tw': 6,
  'ae': 1,
  'us': 43,
  'ye': 28
})
worldmap_chart.render_to_file('bar_chart.svg')



import pygal.maps.world

supra = pygal.maps.world.SupranationalWorld()
supra.add('Asia', [('asia', 1)])
supra.add('Europe', [('europe', 1)])
supra.add('Africa', [('africa', 1)])
supra.add('North america', [('north_america', 1)])
supra.add('South america', [('south_america', 1)])
supra.add('Oceania', [('oceania', 1)])
supra.add('Antartica', [('antartica', 1)])
supra.render_to_file('bar_chart.svg')


x = [1,2,3,4,5]
y = [6,7,8,9,10]
a = zip(x,y)
print (a)