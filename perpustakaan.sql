--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2
-- Dumped by pg_dump version 14.2

-- Started on 2022-04-08 23:50:21

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 209 (class 1259 OID 16396)
-- Name: peminjam; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.peminjam (
    id_peminjam integer NOT NULL,
    nama_peminjam character varying,
    alamat text,
    buku character varying
);


ALTER TABLE public.peminjam OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 16403)
-- Name: peminjam_id_peminjam_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.peminjam ALTER COLUMN id_peminjam ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.peminjam_id_peminjam_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 3305 (class 0 OID 16396)
-- Dependencies: 209
-- Data for Name: peminjam; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.peminjam (id_peminjam, nama_peminjam, alamat, buku) FROM stdin;
2	Azis	Indramayu	Harry Potter
1	Nandia	Bandung	Avengers
\.


--
-- TOC entry 3312 (class 0 OID 0)
-- Dependencies: 210
-- Name: peminjam_id_peminjam_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.peminjam_id_peminjam_seq', 2, true);


--
-- TOC entry 3165 (class 2606 OID 16402)
-- Name: peminjam peminjam_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.peminjam
    ADD CONSTRAINT peminjam_pkey PRIMARY KEY (id_peminjam);


-- Completed on 2022-04-08 23:50:21

--
-- PostgreSQL database dump complete
--

