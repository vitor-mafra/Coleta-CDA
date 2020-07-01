import instaloader
loader = instaloader.Instaloader()
from datetime import datetime

def mostra_atributos(post, username):
	print('\n')
	print('Data de postagem: ' + str(post.date_local))
	print('Localização: ' + str(post.location))
	print('Número de curtidas: ' + str(post.likes))
	print('Usuários marcados: ' + str(post.tagged_users))
	print('Usuários mencionados: ' + str(post.caption_mentions))
	print('\n')


def mostra_comentarios(comment):
	print(comment.text)
	print('Comentado por: ' + str(comment.owner))
	print('Criado em: ' + str(comment.created_at_utc))
	print('Número de curtidas: ' + str(comment.likes_count))
	print('\n')


def mostra_replies(reply):
	print(reply.text)
	print('Comentado por: ' + str(reply.owner))
	print('Criado em: ' + str(reply.created_at_utc))
	print('Número de curtidas: ' + str(reply.likes_count))
	print('\n')


def filtra_comentarios(post, filtro_comments):
	comments = post.get_comments()
	for comment in comments:

		if filtro_comments == '':

			print('Comentários e replies: ')
			print('\n')
			mostra_comentarios(comment)

			replies = comment.answers

			for reply in replies:

				mostra_replies(reply)

		elif filtro_comments in comment.text:

			print('Comentários e replies: ')
			print('\n')
			mostra_comentarios(comment)

			replies = comment.answers

			for reply in replies:

				mostra_replies(reply)


def filtra_datas(post, username, filtro_comments, 
				filtro_temporal_inicio, filtro_temporal_fim):

	if filtro_temporal_inicio == '' and filtro_temporal_fim == '':  # Sem filtro por intervalo de tempo

		mostra_atributos(post, username)

		filtra_comentarios(post, filtro_comments)

	elif filtro_temporal_inicio != '' and filtro_temporal_fim == '' : # Apenas data de início como filtro

		filtro_temporal_inicio = datetime.strptime(filtro_temporal_inicio, "%Y-%m-%d") # Formatação %Y-%m-%d 00:00:00
		
		if post.date_local >= filtro_temporal_inicio:

			mostra_atributos(post, username)

			filtra_comentarios(post, filtro_comments)

		else:

			print('O post não pertence ao intervalo temporal definido.')

	elif filtro_temporal_inicio == '' and filtro_temporal_fim != '': # Apenas data final como filtro

		filtro_temporal_fim = datetime.strptime(filtro_temporal_fim, "%Y-%m-%d") # Formatação %Y-%m-%d 00:00:00

		if post.date_local <= filtro_temporal_fim:

			mostra_atributos(post, username)

			filtra_comentarios(post,filtro_comments)

		else:

			print('O post não pertence ao intervalo temporal definido.')

	else:  # Intervalo de tempo definido como filtro
		
		filtro_temporal_inicio = datetime.strptime(filtro_temporal_inicio, "%Y-%m-%d") # Formatação %Y-%m-%d 00:00:0
		
		filtro_temporal_fim = datetime.strptime(filtro_temporal_fim, "%Y-%m-%d") # Formatação %Y-%m-%d 00:00:00

		if post.date_local >= filtro_temporal_inicio and post.date_local <= filtro_temporal_fim: 

			mostra_atributos(post, username)

			filtra_comentarios(post,filtro_comments)

		else:

			print('O post não pertence ao intervalo temporal definido.')
