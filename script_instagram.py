#!/usr/bin/python

#>>> pip install instaloader
import instaloader

if __name__ == '__main__':
	# >> Para ver os atributos de cada classe e ter mais informacoes: https://instaloader.github.io/as-module.html
	loader = instaloader.Instaloader()

	# O login recebe username e senha como parâmetros, necessário para alguns processos e para a coleta de perfis privados.
	loader.login('', '')

	# Coleta de info de um perfil
	'''
	username = ""
	profile = instaloader.Profile.from_username(loader.context, username)
	user_id = profile.userid
	full_name = profile.full_name
	print('Name: ' + str(full_name) + '  --  ID: ' + str(user_id))
	print('Private? ' + str(profile.is_private))
	print('\n')
	loader.download_profilepic(profile)
	loader.download_tagged(profile, fast_update=False, target=None, post_filter=None)
	'''
	#Coleta highlights de um perfil
	# >> Precisa estar logado
	'''
	for highlight in loader.get_highlights(profile):
		for item in highlight.get_items():
			loader.download_storyitem(item, '{}/{}'.format(highlight.owner_username, highlight.title))
	'''
	# Coleta posts de um perfil
	'''
	posts = profile.get_posts()

	counter = 1
	for post in posts:
	
		print('Post ' + str(counter))
		loader.download_post(post, username)
		print(post.caption)
		print(post.owner_profile)
		print('Data de postagem: ' + str(post.date_local))
		#print('tagged users: '+str(post.tagged_users))
	'''
		# Com um post voce pode coletar os comments e com um comment, as replies dele
	'''
		comments = post.get_comments()

		for comment in comments:
			print(comment.text)
			replies = comment.answers

			for reply in replies:
				pass

		print('\n')
		counter += 1
	'''
	# Coleta da rede do perfil
	# >> para esse tipo de coleta tem que logar no Instagram
	'''
	loader.login("usuario","password")
	followers = profile.get_followers()
	followees = seed_user_profile.get_followees()

	for follower in followers:
		pass
	'''
	# Coleta de stories de um perfil
	# >> para esse tipo de coleta tambem tem que logar no Instagram
	'''
	loader.download_stories(userids=[profile.userid], filename_target='{}'.format(profile.username), fast_update=True)
	'''
	# Coleta info de uma hashtag
	'''
	tag = "coronavirus"
	hashtag = instaloader.Hashtag.from_name(loader.context, tag)
	tag_id = hashtag.hashtagid
	print('Hashtag: #' + str(hashtag.name) + '  --  ID: ' + str(tag_id))
	print('Posts count: ' + str(hashtag.mediacount))
	print('\n')
	#Faz download dos posts associados com a hashtag
	for post in hashtag.get_posts():
		loader.download_post(post, target="#"+hashtag.name)
	'''
