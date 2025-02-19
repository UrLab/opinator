podman run --rm --name bebou --volume /home/$USER/opinator/software/logs:/logs --env-file .env --network host opinator:http
