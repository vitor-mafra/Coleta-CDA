#>>> pip install instaloader
import instaloader
from datetime import datetime #Formatação do formato das datas

if __name__ == '__main__':
    	
	# >> Para ver os atributos de cada classe e ter mais informacoes: https://instaloader.github.io/as-module.html
	loader = instaloader.Instaloader()

	# O interactive_login recebe username como parâmetro, necessário para alguns processos e para a coleta de perfis privados.
	# A senha deve ser preenchida no terminal.
	loader.interactive_login('julia_stancioli')
	
	#Download das publicações no feed, é possível filtrar os posts (ex.: o usuário curtiu)
	'''
	loader.get_feed_posts()
	loader.download_feed_posts(max_count=5, fast_update=True, post_filter=None)
	'''

	# Coleta de info de um perfil
	
	username = "julia_stancioli"
	profile = instaloader.Profile.from_username(loader.context, username)
	user_id = profile.userid
	full_name = profile.full_name
	print('Name: ' + str(full_name) + '  --  ID: ' + str(user_id))
	print('Private? ' + str(profile.is_private))
	print('\n')
	

	#Download da imagem de perfil do usuário
	'''
	loader.download_profilepic(profile)
	'''

	# Download dos posts em que o usuário foi marcado
	'''
	usuario = "--username--" #usar somente quando a info do perfil estiver comentada
	profile = instaloader.Profile.from_username(loader.context, usuario)
	loader.download_tagged(profile, fast_update=False, target=None, post_filter=None)
	'''

	#Coleta highlights de um perfil
	# >> É necessário estar logado no Instagram
	'''
	for highlight in loader.get_highlights(profile):
		for item in highlight.get_items():
			loader.download_storyitem(item, '{}/{}'.format(highlight.owner_username, highlight.title))
	'''

	# Coleta posts de um perfil
	# >> É necessário seguir o perfil privado para coletar essas informações
	
	posts = profile.get_posts()

	filtro_temporal_inicio = '2019-01-19' # Formato %Y-%m-%d 
	filtro_temporal_inicio = datetime.strptime(filtro_temporal_inicio, "%Y-%m-%d") # Formatação %Y-%m-%d 00:00:00

	filtro_temporal_fim = '2019-02-04'  # Formato %Y-%m-%d 
	filtro_temporal_fim = datetime.strptime(filtro_temporal_fim, "%Y-%m-%d") # Formatação %Y-%m-%d 00:00:00

	filtro_posts = '' # Palavra-chave de interesse na legenda

	filtro_comments = '' # Palavra-chave de interesse nos comentários

	counter = 1
	for post in posts:
    		
		# Com um post voce pode coletar os comments e com um comment, os replies dele
		comments = post.get_comments()
	
		print('Post ' + str(counter)) # Contagem dos posts

		if filtro_posts == '': # Sem filtro de palavra-chave

			if filtro_temporal_inicio == '' and filtro_temporal_fim == '': # Sem filtro por intervalo de tempo

				loader.download_post(post, username)
				print('Sponsored? ' + str(post.is_sponsored))
				if post.is_sponsored == True:
					print('Patrocinadores: ' + str(post.sponsor_users))
				print('Legenda do post: "' + str(post.caption) + '"')
				print(post.owner_profile)
				print('Data de postagem: ' + str(post.date_local))
				print('Localização: ' + str(post.location))
				print('Número de curtidas: ' + str(post.likes))
				print('Usuários marcados: ' + str(post.tagged_users))
				print('Usuários mencionados: ' + str(post.caption_mentions))
				print('\n')
				print('Comentários e replies: ')

				for comment in comments:
					
					if filtro_comments == '':
    						
						print(comment.text)
						print('Comentado por: ' + str(comment.owner))
						print('Criado em: ' + str(comment.created_at_utc))
						print('Número de curtidas: ' + str(comment.likes_count))

						replies = comment.answers

						for reply in replies:

							print(reply.text)
							print('Comentado por: ' + str(reply.owner))
							print('Criado em: ' + str(reply.created_at_utc))
							print('Número de curtidas: ' + str(reply.likes_count))

					elif filtro_comments in comment.text:

						print(comment.text)
						print('Comentado por: ' + str(comment.owner))
						print('Criado em: ' + str(comment.created_at_utc))
						print('Número de curtidas: ' + str(comment.likes_count))
						
						replies = comment.answers

						for reply in replies:
								
							print(reply.text)
							print('Comentado por: ' + str(reply.owner))
							print('Criado em: ' + str(reply.created_at_utc))
							print('Número de curtidas: ' + str(reply.likes_count))

			elif filtro_temporal_inicio != '' and filtro_temporal_fim == '' : # Apenas data de início como filtro

				if post.date_local >= filtro_temporal_inicio:
    					
					loader.download_post(post, username)
					print('Sponsored? ' + str(post.is_sponsored))
					if post.is_sponsored == True:
						print('Patrocinadores: ' + str(post.sponsor_users))
					print('Legenda do post: "' + str(post.caption) + '"')
					print(post.owner_profile)
					print('Data de postagem: ' + str(post.date_local))
					print('Localização: ' + str(post.location))
					print('Número de curtidas: ' + str(post.likes))
					print('Usuários marcados: ' + str(post.tagged_users))
					print('Usuários mencionados: ' + str(post.caption_mentions))
					print('\n')
					print('Comentários e replies: ')

					for comment in comments:
    						
						if filtro_comments == '':
    						
							print(comment.text)
							print('Comentado por: ' + str(comment.owner))
							print('Criado em: ' + str(comment.created_at_utc))
							print('Número de curtidas: ' + str(comment.likes_count))

							replies = comment.answers

							for reply in replies:

								print(reply.text)
								print('Comentado por: ' + str(reply.owner))
								print('Criado em: ' + str(reply.created_at_utc))
								print('Número de curtidas: ' + str(reply.likes_count))

						elif filtro_comments in comment.text:

							print(comment.text)
							print('Comentado por: ' + str(comment.owner))
							print('Criado em: ' + str(comment.created_at_utc))
							print('Número de curtidas: ' + str(comment.likes_count))
							
							replies = comment.answers

							for reply in replies:
									
								print(reply.text)
								print('Comentado por: ' + str(reply.owner))
								print('Criado em: ' + str(reply.created_at_utc))
								print('Número de curtidas: ' + str(reply.likes_count))

				else:
    							
					print('O post não pertence ao intervalo temporal definido.')

			elif filtro_temporal_inicio == '' and filtro_temporal_fim != '': # Apenas data final como filtro
    				
				if post.date_local <= filtro_temporal_fim:
    					
					loader.download_post(post, username)
					print('Sponsored? ' + str(post.is_sponsored))
					if post.is_sponsored == True:
						print('Patrocinadores: ' + str(post.sponsor_users))
					print('Legenda do post: "' + str(post.caption) + '"')
					print(post.owner_profile)
					print('Data de postagem: ' + str(post.date_local))
					print('Localização: ' + str(post.location))
					print('Número de curtidas: ' + str(post.likes))
					print('Usuários marcados: ' + str(post.tagged_users))
					print('Usuários mencionados: ' + str(post.caption_mentions))
					print('\n')
					print('Comentários e replies: ')

					for comment in comments:

						if filtro_comments == '':

							print(comment.text)
							print('Comentado por: ' + str(comment.owner))
							print('Criado em: ' + str(comment.created_at_utc))
							print('Número de curtidas: ' + str(comment.likes_count))

							replies = comment.answers

							for reply in replies:

								print(reply.text)
								print('Comentado por: ' + str(reply.owner))
								print('Criado em: ' + str(reply.created_at_utc))
								print('Número de curtidas: ' + str(reply.likes_count))

						elif filtro_comments in comment.text:

							print(comment.text)
							print('Comentado por: ' + str(comment.owner))
							print('Criado em: ' + str(comment.created_at_utc))
							print('Número de curtidas: ' + str(comment.likes_count))

							replies = comment.answers

							for reply in replies:

								print(reply.text)
								print('Comentado por: ' + str(reply.owner))
								print('Criado em: ' + str(reply.created_at_utc))
								print('Número de curtidas: ' + str(reply.likes_count))

				else:
    							
					print('O post não pertence ao intervalo temporal definido.')

			else:  # Intervalo de tempo definido como filtro
    				
				if post.date_local >= filtro_temporal_inicio and post.date_local <= filtro_temporal_fim: 
    					
					loader.download_post(post, username)
					print('Sponsored? ' + str(post.is_sponsored))
					if post.is_sponsored == True:
						print('Patrocinadores: ' + str(post.sponsor_users))
					print('Legenda do post: "' + str(post.caption) + '"')
					print(post.owner_profile)
					print('Data de postagem: ' + str(post.date_local))
					print('Localização: ' + str(post.location))
					print('Número de curtidas: ' + str(post.likes))
					print('Usuários marcados: ' + str(post.tagged_users))
					print('Usuários mencionados: ' + str(post.caption_mentions))
					print('\n')
					print('Comentários e replies: ')

					for comment in comments:

						if filtro_comments == '':

							print(comment.text)
							print('Comentado por: ' + str(comment.owner))
							print('Criado em: ' + str(comment.created_at_utc))
							print('Número de curtidas: ' + str(comment.likes_count))

							replies = comment.answers

							for reply in replies:

								print(reply.text)
								print('Comentado por: ' + str(reply.owner))
								print('Criado em: ' + str(reply.created_at_utc))
								print('Número de curtidas: ' + str(reply.likes_count))

						elif filtro_comments in comment.text:

							print(comment.text)
							print('Comentado por: ' + str(comment.owner))
							print('Criado em: ' + str(comment.created_at_utc))
							print('Número de curtidas: ' + str(comment.likes_count))

							replies = comment.answers

							for reply in replies:

								print(reply.text)
								print('Comentado por: ' + str(reply.owner))
								print('Criado em: ' + str(reply.created_at_utc))
								print('Número de curtidas: ' + str(reply.likes_count))

				else:
    			
					print('O post não pertence ao intervalo temporal definido.')

		elif post.caption is not None:
    			
			if filtro_posts in post.caption: #Filtro por palavra-chave
    				
				if filtro_temporal_inicio == '' and filtro_temporal_fim == '': # Sem filtro por intervalo de tempo
    					
					loader.download_post(post, username)
					print('Sponsored? ' + str(post.is_sponsored))
					if post.is_sponsored == True:
						print('Patrocinadores: ' + str(post.sponsor_users))
					print('Legenda do post: "' + str(post.caption) + '"')
					print(post.owner_profile)
					print('Data de postagem: ' + str(post.date_local))
					print('Localização: ' + str(post.location))
					print('Número de curtidas: ' + str(post.likes))
					print('Usuários marcados: ' + str(post.tagged_users))
					print('Usuários mencionados: ' + str(post.caption_mentions))
					print('\n')
					print('Comentários e replies: ')

					for comment in comments:

						if filtro_comments == '':

							print(comment.text)
							print('Comentado por: ' + str(comment.owner))
							print('Criado em: ' + str(comment.created_at_utc))
							print('Número de curtidas: ' + str(comment.likes_count))

							replies = comment.answers

							for reply in replies:

								print(reply.text)
								print('Comentado por: ' + str(reply.owner))
								print('Criado em: ' + str(reply.created_at_utc))
								print('Número de curtidas: ' + str(reply.likes_count))

						elif filtro_comments in comment.text:

							print(comment.text)
							print('Comentado por: ' + str(comment.owner))
							print('Criado em: ' + str(comment.created_at_utc))
							print('Número de curtidas: ' + str(comment.likes_count))

							replies = comment.answers

							for reply in replies:

								print(reply.text)
								print('Comentado por: ' + str(reply.owner))
								print('Criado em: ' + str(reply.created_at_utc))
								print('Número de curtidas: ' + str(reply.likes_count))

				elif filtro_temporal_inicio != '' and filtro_temporal_fim == '' : # Apenas data de início como filtro
    					
					if post.date_local >= filtro_temporal_inicio:
    						
						loader.download_post(post, username)
						print('Sponsored? ' + str(post.is_sponsored))
						if post.is_sponsored == True:
							print('Patrocinadores: ' + str(post.sponsor_users))
						print('Legenda do post: "' + str(post.caption) + '"')
						print(post.owner_profile)
						print('Data de postagem: ' + str(post.date_local))
						print('Localização: ' + str(post.location))
						print('Número de curtidas: ' + str(post.likes))
						print('Usuários marcados: ' + str(post.tagged_users))
						print('Usuários mencionados: ' + str(post.caption_mentions))
						print('\n')
						print('Comentários e replies: ')

						for comment in comments:

							if filtro_comments == '':

								print(comment.text)
								print('Comentado por: ' + str(comment.owner))
								print('Criado em: ' + str(comment.created_at_utc))
								print('Número de curtidas: ' + str(comment.likes_count))

								replies = comment.answers

								for reply in replies:

									print(reply.text)
									print('Comentado por: ' + str(reply.owner))
									print('Criado em: ' + str(reply.created_at_utc))
									print('Número de curtidas: ' + str(reply.likes_count))

							elif filtro_comments in comment.text:

								print(comment.text)
								print('Comentado por: ' + str(comment.owner))
								print('Criado em: ' + str(comment.created_at_utc))
								print('Número de curtidas: ' + str(comment.likes_count))

								replies = comment.answers

								for reply in replies:

									print(reply.text)
									print('Comentado por: ' + str(reply.owner))
									print('Criado em: ' + str(reply.created_at_utc))
									print('Número de curtidas: ' + str(reply.likes_count))

					else:
    							
						print('O post não pertence ao intervalo temporal definido.')

				elif filtro_temporal_inicio == '' and filtro_temporal_fim != '': # Apenas data final como filtro

					if post.date_local <= filtro_temporal_fim:
    						
						loader.download_post(post, username)
						print('Sponsored? ' + str(post.is_sponsored))
						if post.is_sponsored == True:
							print('Patrocinadores: ' + str(post.sponsor_users))
						print('Legenda do post: "' + str(post.caption) + '"')
						print(post.owner_profile)
						print('Data de postagem: ' + str(post.date_local))
						print('Localização: ' + str(post.location))
						print('Número de curtidas: ' + str(post.likes))
						print('Usuários marcados: ' + str(post.tagged_users))
						print('Usuários mencionados: ' + str(post.caption_mentions))
						print('\n')
						print('Comentários e replies: ')

						for comment in comments:

							if filtro_comments == '':

								print(comment.text)
								print('Comentado por: ' + str(comment.owner))
								print('Criado em: ' + str(comment.created_at_utc))
								print('Número de curtidas: ' + str(comment.likes_count))

								replies = comment.answers

								for reply in replies:

									print(reply.text)
									print('Comentado por: ' + str(reply.owner))
									print('Criado em: ' + str(reply.created_at_utc))
									print('Número de curtidas: ' + str(reply.likes_count))

							elif filtro_comments in comment.text:

								print(comment.text)
								print('Comentado por: ' + str(comment.owner))
								print('Criado em: ' + str(comment.created_at_utc))
								print('Número de curtidas: ' + str(comment.likes_count))

								replies = comment.answers

								for reply in replies:

									print(reply.text)
									print('Comentado por: ' + str(reply.owner))
									print('Criado em: ' + str(reply.created_at_utc))
									print('Número de curtidas: ' + str(reply.likes_count))

					else:
    							
						print('O post não pertence ao intervalo temporal definido.')

				else: # Intervalo de tempo definido como filtro
    					
					if post.date_local >= filtro_temporal_inicio and post.date_local <= filtro_temporal_fim:
    						
						loader.download_post(post, username)
						print('Sponsored? ' + str(post.is_sponsored))
						if post.is_sponsored == True:
							print('Patrocinadores: ' + str(post.sponsor_users))
						print('Legenda do post: "' + str(post.caption) + '"')
						print(post.owner_profile)
						print('Data de postagem: ' + str(post.date_local))
						print('Localização: ' + str(post.location))
						print('Número de curtidas: ' + str(post.likes))
						print('Usuários marcados: ' + str(post.tagged_users))
						print('Usuários mencionados: ' + str(post.caption_mentions))
						print('\n')
						print('Comentários e replies: ')

						for comment in comments:

							if filtro_comments == '':

								print(comment.text)
								print('Comentado por: ' + str(comment.owner))
								print('Criado em: ' + str(comment.created_at_utc))
								print('Número de curtidas: ' + str(comment.likes_count))

								replies = comment.answers

								for reply in replies:

									print(reply.text)
									print('Comentado por: ' + str(reply.owner))
									print('Criado em: ' + str(reply.created_at_utc))
									print('Número de curtidas: ' + str(reply.likes_count))

							elif filtro_comments in comment.text:

								print(comment.text)
								print('Comentado por: ' + str(comment.owner))
								print('Criado em: ' + str(comment.created_at_utc))
								print('Número de curtidas: ' + str(comment.likes_count))

								replies = comment.answers

								for reply in replies:

									print(reply.text)
									print('Comentado por: ' + str(reply.owner))
									print('Criado em: ' + str(reply.created_at_utc))
									print('Número de curtidas: ' + str(reply.likes_count))
					
					else:
							
						print('O post não pertence ao intervalo temporal definido.')

			else:
    				
    			 print('A legenda do post não contém a palavra "' + filtro_posts + '"')
		 

		print('\n')
		counter += 1
    
	
	# Coleta da rede do perfil
	# >> É necessário estar logado no Instagram
	'''
	followers = profile.get_followers()
	followees = seed_user_profile.get_followees()

	for follower in followers:
		pass
	'''

	# Coleta de stories de um perfil
	# >> É necessário estar logado no Instagram
	'''
	loader.download_stories(userids=[profile.userid], filename_target='{}'.format(profile.username), fast_update=True)
	'''

	# Coleta info de uma hashtag
	'''
	tag = "--nome_da_hashtag--"
	hashtag = instaloader.Hashtag.from_name(loader.context, tag)
	tag_id = hashtag.hashtagid
	print('Hashtag: #' + str(hashtag.name) + '  --  ID: ' + str(tag_id))
	print('Posts count: ' + str(hashtag.mediacount))
	print('\n')
	#Faz download dos posts associados com a hashtag
	for post in hashtag.get_posts():
		loader.download_post(post, target="#"+hashtag.name)
	'''
