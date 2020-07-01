#>>> pip install instaloader
import instaloader
import posts_module
from datetime import datetime #Formatação do formato das datas


if __name__ == '__main__':

	# >> Para ver os atributos de cada classe e ter mais informacoes: https://instaloader.github.io/as-module.html
	loader = instaloader.Instaloader()

	# O interactive_login recebe username como parâmetro, necessário para alguns processos e para a coleta de perfis privados.
	# A senha deve ser preenchida no terminal.
	loader.interactive_login('julia_stancioli')

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

	# Coleta posts de um perfil
	# >> É necessário seguir o perfil privado para coletar essas informações
	
	posts = profile.get_posts()

	filtro_temporal_inicio = '' # Formato %Y-%m-%d ou vazio

	filtro_temporal_fim = ''  # Formato %Y-%m-%d ou vazio

	filtro_posts = '' # Palavra-chave de interesse na legenda

	filtro_comments = '' # Palavra-chave de interesse nos comentários

	numero_do_post = 1 # Enumerando os posts para fins de organizacao
	for post in posts:
	
		print('Post ' + str(numero_do_post)) # Contagem dos posts

		if filtro_posts == '': # Sem filtro de palavra-chave	

			posts_module.filtra_datas(post, username, filtro_comments, filtro_temporal_inicio, filtro_temporal_fim)

		elif post.caption is not None:

			posts_module.filtra_datas(post, username, filtro_comments, filtro_temporal_inicio, filtro_temporal_fim)

		else:
    		 print('A legenda do post não contém a palavra "' + filtro_posts + '"')


		print('\n')
		numero_do_post += 1