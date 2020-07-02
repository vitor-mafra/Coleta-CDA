import instaloader
loader = instaloader.Instaloader()
from datetime import datetime

'''
A função "mostra_atributos" recebe como parâmetros post e usuário (username) e exibe no terminal as informações "Data de postagem", 
"Localização", "Número de curtidas", "Usuários marcados" e "Usuários mencionados" para cada um dos posts de um dado usuário.
'''
def mostra_atributos(post, username):
	print('\n')
	print('Data de postagem: ' + str(post.date_local))
	print('Localização: ' + str(post.location))
	print('Número de curtidas: ' + str(post.likes))
	print('Usuários marcados: ' + str(post.tagged_users))
	print('Usuários mencionados: ' + str(post.caption_mentions))
	print('\n')


'''
A função "mostra_comentarios" recebe como parâmetro o comentário (comment) e exibe no terminal as informações 
"Comentado por", "Criado em" e "Número de curtidas" para cada um dos comentários de um dado post.
'''
def mostra_comentarios(comment):
	print(comment.text)
	print('Comentado por: ' + str(comment.owner))
	print('Criado em: ' + str(comment.created_at_utc))
	print('Número de curtidas: ' + str(comment.likes_count))
	print('\n')


'''
A função "mostra_replies" recebe como parâmetro a reply e exibe no terminal as informações "Comentado por", 
"Criado em" e "Número de curtidas" para cada uma das replies de um dado comentário.
'''
def mostra_replies(reply):
	print(reply.text)
	print('Comentado por: ' + str(reply.owner))
	print('Criado em: ' + str(reply.created_at_utc))
	print('Número de curtidas: ' + str(reply.likes_count))
	print('\n')


'''
A função "filtra_comentarios" recebe como parâmetros o post, a palavra-chave de interesse nos comentários (filtro_comments)
e a palavra-chave de interesse nas replies (filtro_replies). Ela busca todos os comentários do post e retorna para a função
"mostra_comentarios" apenas os que contêm a palavra-chave de interesse.
'''
def filtra_comentarios(post, filtro_comments, filtro_replies):
	comments = post.get_comments()
	if comments is not None:
		print('Comentários: ')
		print('\n')

		for comment in comments:

			if filtro_comments == '':
				mostra_comentarios(comment)
				filtra_replies(comment, filtro_replies)

			elif filtro_comments in comment.text:
				mostra_comentarios(comment)
				filtra_replies(comment, filtro_replies)


'''
A função "filtra_replies" recebe como parâmetros o comentário (comment) e a palavra-chave de interesse nas replies (filtro_replies).
Ela busca todas as replies do comentário e retorna para a função "mostra_replies" apenas as que contêm a palavra-chave de interesse.
'''
def filtra_replies(comment, filtro_replies):
	replies = comment.answers
	if replies is not None: 				

		numero_da_reply = 1 # Contagem das replies

		for reply in replies:
			print('Reply ' + str(numero_da_reply))
			print('\n')
				
			if filtro_replies == '':
				mostra_replies(reply)

			elif filtro_replies in reply.text:
				mostra_replies(reply)
			
			else:
				print('A reply não contém a palavra "' + str(filtro_replies) + '"')
			
			numero_da_reply += 1


'''
A função "filtra_datas" recebe como parâmetros o número do post, o post, o usuário (username), a palavra-chave de interesse nos 
comentários (filtro_comments), a palavra-chave de interesse nas replies (filtro_replies), a data inicial (filto_temporal_inicio) 
e a data final para coleta de dados (filtro_temporal_fim). Ela seleciona apenas os posts que pertencem ao intervalo temporal
definido e os retorna para a função "download_componentes".

'''
def filtra_datas(numero_do_post, post, username, filtro_comments, filtro_replies,
				filtro_temporal_inicio, filtro_temporal_fim):

	if filtro_temporal_inicio == '' and filtro_temporal_fim == '':  # Sem filtro por intervalo de tempo
		download_componentes(numero_do_post, post, username, filtro_comments, filtro_replies)

	elif filtro_temporal_inicio != '' and filtro_temporal_fim == '' : # Apenas data de início como filtro
		filtro_temporal_inicio = datetime.strptime(filtro_temporal_inicio, "%Y-%m-%d") # Formatação %Y-%m-%d 00:00:00
		
		if post.date_local >= filtro_temporal_inicio:
			download_componentes(numero_do_post, post, username, filtro_comments, filtro_replies)

	elif filtro_temporal_inicio == '' and filtro_temporal_fim != '': # Apenas data final como filtro
		filtro_temporal_fim = datetime.strptime(filtro_temporal_fim, "%Y-%m-%d") # Formatação %Y-%m-%d 00:00:00

		if post.date_local <= filtro_temporal_fim:
			download_componentes(numero_do_post, post, username, filtro_comments, filtro_replies)

	else:  # Intervalo de tempo definido como filtro
		filtro_temporal_inicio = datetime.strptime(filtro_temporal_inicio, "%Y-%m-%d") # Formatação %Y-%m-%d 00:00:0
		filtro_temporal_fim = datetime.strptime(filtro_temporal_fim, "%Y-%m-%d") # Formatação %Y-%m-%d 00:00:00

		if post.date_local >= filtro_temporal_inicio and post.date_local <= filtro_temporal_fim: 
			download_componentes(numero_do_post, post, username, filtro_comments, filtro_replies)



'''
A função "download_componentes" recebe como parâmetros o número do post, o post, o usuário (username), a palavra-chave de interesse nos comentários
(filtro_comments) e a palavra-chave de interesse nas replies (filtro_replies). Ela faz o download do post e retorna as funções 
"mostra_atributos" e "filtra_comentarios".
'''
def download_componentes(numero_do_post, post, username, filtro_comments, filtro_replies):
    
	print('Post ' + str(numero_do_post))

	loader.download_post(post, username)
	mostra_atributos(post, username)
	filtra_comentarios(post, filtro_comments, filtro_replies)

	print('\n')
