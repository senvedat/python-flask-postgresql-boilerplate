PGDMP                         z            vdt-flask-reporting-example    14.5    14.4     ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    26826    vdt-flask-reporting-example    DATABASE     ?   CREATE DATABASE "vdt-flask-reporting-example" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United Kingdom.1254';
 -   DROP DATABASE "vdt-flask-reporting-example";
                postgres    false            ?            1259    26834    transaction    TABLE     ?   CREATE TABLE public.transaction (
    id integer NOT NULL,
    merchant integer,
    acquirer integer,
    currency character varying,
    amount integer,
    transactiondate timestamp without time zone
);
    DROP TABLE public.transaction;
       public         heap    postgres    false            ?            1259    26833    data_id_seq    SEQUENCE     ?   ALTER TABLE public.transaction ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.data_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    212            ?            1259    26828    users    TABLE     }   CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying(128),
    password character varying(32)
);
    DROP TABLE public.users;
       public         heap    postgres    false            ?            1259    26827    users_id_seq    SEQUENCE     ?   ALTER TABLE public.users ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    210            ?          0    26834    transaction 
   TABLE DATA           `   COPY public.transaction (id, merchant, acquirer, currency, amount, transactiondate) FROM stdin;
    public          postgres    false    212   G       ?          0    26828    users 
   TABLE DATA           4   COPY public.users (id, email, password) FROM stdin;
    public          postgres    false    210   ?       ?           0    0    data_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('public.data_id_seq', 4, true);
          public          postgres    false    211            ?           0    0    users_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.users_id_seq', 3, true);
          public          postgres    false    209            d           2606    26840    transaction data_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.transaction
    ADD CONSTRAINT data_pkey PRIMARY KEY (id);
 ?   ALTER TABLE ONLY public.transaction DROP CONSTRAINT data_pkey;
       public            postgres    false    212            b           2606    26832    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    210            ?   A   x?3?4?4?v?44?4202?5"c+0?2B(???????)???	&pfX??qqq ZKm      ?   8   x?3??M-J?H?+q(I-.?K???44261?2?L?M???,H,..?/J?????? y?     